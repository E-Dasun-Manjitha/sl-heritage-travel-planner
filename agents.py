import os
import json
# pyrefly: ignore [missing-import]
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

# 1. API Keys Retrieval
groq_key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))
openrouter_key = st.secrets.get("OPENROUTER_API_KEY", os.getenv("OPENROUTER_API_KEY"))

# Fallbacks for local testing if secrets are empty/placeholder
if not groq_key or groq_key == "your_actual_groq_api_key_here":
    groq_key = os.getenv("GROQ_API_KEY")
if not openrouter_key or openrouter_key == "your_actual_openrouter_api_key_here":
    openrouter_key = os.getenv("OPENROUTER_API_KEY")

# 2. Model Initialization (Deliberate Model Strategy)
def get_fast_router_llm():
    if not groq_key:
        raise ValueError("GROQ_API_KEY is not configured! Please set it in .streamlit/secrets.toml.")
    return ChatGroq(
        model_name="llama-3.1-8b-instant",
        groq_api_key=groq_key,
        temperature=0.2
    )

def get_reasoning_architect_llm():
    if not openrouter_key:
        raise ValueError("OPENROUTER_API_KEY is not configured! Please set it in .streamlit/secrets.toml.")
    return ChatOpenAI(
        model="openai/gpt-4o-mini",
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=openrouter_key,
        temperature=0.4
    )

# 3. Vector Database Connection
# Check if chroma_db exists first
if os.path.exists("./chroma_db"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
else:
    vector_db = None

def agent_1_logistics_specialist(user_interests, user_days):
    """
    Agent 1 (Tool-Use & Router Pattern):
    Queries the vector DB, extracts factual context, and structures regional logistics and pricing.
    """
    if vector_db is None:
        return json.dumps({"error": "Vector database not found. Please run rag_builder.py first."}), []
        
    # Construct search query based on user options (Router Pattern)
    query = f"Attractions, entry ticket costs, dress codes, and transport for {user_interests} in {user_days} days"
    
    # Retrieve top 5 matching document chunks (Tool-Use Pattern)
    retrieved_docs = vector_db.similarity_search(query, k=5)
    context_text = "\n\n".join([f"Source {i+1} ({doc.metadata.get('source', 'Unknown')}):\n{doc.page_content}" for i, doc in enumerate(retrieved_docs)])
    
    prompt = f"""
    You are Agent 1 (Logistics Specialist).
    Your task is to review the retrieved tourist facts and organize them into a structured JSON payload for the Itinerary Architect.
    
    Retrieved Context:
    {context_text}
    
    User Parameters:
    - Interests: {user_interests}
    - Days: {user_days}
    
    Instructions:
    Extract facts strictly from the context above. Group them by:
    1. attractions (name, entrance fee in LKR or USD, and mandatory dress code rules)
    2. transport_choices (types, estimated costs in LKR, and booking requirements)
    3. general_rules (temple etiquettes, monsoons, clothing guides)
    
    You MUST respond ONLY with a valid JSON block containing:
    {{
      "attractions": [
        {{"name": "...", "fee": "...", "dress_code": "..."}}
      ],
      "transport_choices": [
        {{"type": "...", "cost_estimate": "...", "booking_tips": "..."}}
      ],
      "cultural_and_safety_rules": ["..."]
    }}
    Do not add any conversational text before or after the JSON.
    """
    
    fast_llm = get_fast_router_llm()
    response = fast_llm.invoke(prompt)
    
    # Extract JSON content if the model outputs code blocks
    content = response.content.strip()
    if content.startswith("```json"):
        content = content[7:]
    if content.endswith("```"):
        content = content[:-3]
    content = content.strip()
    
    return content, retrieved_docs

def agent_2_itinerary_architect(extracted_logistics_json, user_budget, user_days):
    """
    Agent 2 (Reflection & Orchestrator Pattern):
    Receives structured output from Agent 1 and builds a day-by-day plan adhering to constraints.
    Performs a reflection loop checking the budget.
    """
    # Parse the logistics payload (Agent-to-Agent communication)
    try:
        logistics_data = json.loads(extracted_logistics_json)
    except Exception:
        logistics_data = {"error": "Could not parse JSON payload from Agent 1", "raw": extracted_logistics_json}
        
    prompt = f"""
    You are Agent 2 (Itinerary Architect).
    You will create a custom {user_days}-Day Travel Itinerary for Sri Lanka.
    
    Logistics Data payload from Agent 1:
    {json.dumps(logistics_data, indent=2)}
    
    Constraints:
    - Duration: {user_days} Days
    - Max Budget limit: {user_budget} LKR
    
    Instructions:
    1. **Drafting Step**: Build a day-by-day schedule (Morning, Afternoon, Evening) matching the user's interests.
    2. **Self-Reflection & Budget Verification**:
       - Sum up all mandatory entrance fees and transport costs mentioned in the itinerary.
       - Verify if the total fits strictly within {user_budget} LKR.
       - If it exceeds, adjust: swap out expensive destinations (e.g., Sigiriya @ $35 USD or park safari jeeps @ 15,000 LKR) with free/affordable alternatives (e.g., Galle Fort, beaches, or hiking Little Adam's Peak which are free).
    3. **Output Format**:
       Create a beautiful markdown itinerary. Begin with a "Budget Analysis & Verification Report" containing:
       - Total estimated cost (Fees + Transport)
       - Verification status (Passed / Adjusted to fit budget)
       - If adjusted, list what expensive options were removed/swapped.
       Then output the Day-by-Day plan with clean formatting, emoji indicators, and tips.
    """
    
    reasoning_llm = get_reasoning_architect_llm()
    response = reasoning_llm.invoke(prompt)
    return response.content
