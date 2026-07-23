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

def agent_1_logistics_specialist(user_interests, user_days, accommodation_tier="Mid-Range"):
    """
    Agent 1 (Tool-Use & Router Pattern):
    Queries the vector DB for attractions, accommodation, adventure packages, emergency hotlines, and transport.
    Structures a comprehensive logistics JSON payload for Agent 2.
    """
    if vector_db is None:
        return json.dumps({"error": "Vector database not found. Please run rag_builder.py first."}), []
        
    # Construct targeted search query combining interests, accommodation tier, and essential rules (Router Pattern)
    query = f"Attractions, entry ticket fees, {accommodation_tier} accommodation, transport apps, emergency hotlines, Hela Bojun dining, permits, and dress codes for {user_interests} in {user_days} days"
    
    # Retrieve top 10 matching document chunks across the 100-document knowledge base (Tool-Use Pattern)
    retrieved_docs = vector_db.similarity_search(query, k=10)
    context_text = "\n\n".join([f"Source {i+1} ({doc.metadata.get('source', 'Unknown')}):\n{doc.page_content}" for i, doc in enumerate(retrieved_docs)])
    
    prompt = f"""
    You are Agent 1 (Logistics Specialist).
    Your task is to review the retrieved tourist facts and organize them into a structured JSON payload for the Itinerary Architect.
    
    Retrieved Context:
    {context_text}
    
    User Parameters:
    - Interests: {user_interests}
    - Days: {user_days}
    - Preferred Accommodation Tier: {accommodation_tier}
    
    Instructions:
    Extract facts strictly from the context above. Group them by:
    1. attractions (name, entrance fee in LKR or USD, dress code or permit rules)
    2. accommodation_options (category, price range, recommended places)
    3. transport_and_apps (ride-hailing coverage, expressways, driving permits)
    4. emergency_and_police_hotlines (tourist police 1912, ambulance 1990, disaster 117, hospitals)
    5. dining_and_hela_bojun (Hela Bojun outlets, local food price ranges)
    6. permits_and_safety_rules (temple etiquettes, DWC online permits, drone rules)
    
    You MUST respond ONLY with a valid JSON block containing:
    {{
      "attractions": [
        {{"name": "...", "fee": "...", "rules": "..."}}
      ],
      "accommodation_options": [
        {{"tier": "...", "location": "...", "price_range": "...", "options": "..."}}
      ],
      "transport_and_apps": [
        {{"service": "...", "details": "..."}}
      ],
      "emergency_and_police_hotlines": [
        {{"facility": "...", "contact": "...", "role": "..."}}
      ],
      "dining_and_hela_bojun": [
        {{"outlet": "...", "details": "..."}}
      ],
      "permits_and_safety_rules": ["..."]
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

def agent_2_itinerary_architect(extracted_logistics_json, user_budget, user_days, accommodation_tier="Mid-Range"):
    """
    Agent 2 (Reflection & Orchestrator Pattern):
    Receives structured output from Agent 1 and builds a day-by-day plan adhering to constraints.
    Performs a reflection loop checking the total budget (fees + accommodation + transport).
    Appends full guidelines (emergency hotlines, transport hacks, dining, and permits).
    """
    # Parse the logistics payload (Agent-to-Agent communication)
    try:
        logistics_data = json.loads(extracted_logistics_json)
    except Exception:
        logistics_data = {"error": "Could not parse JSON payload from Agent 1", "raw": extracted_logistics_json}
        
    prompt = f"""
    You are Agent 2 (Itinerary Architect).
    You will create a comprehensive, high-value {user_days}-Day Travel Itinerary & Guidelines for Sri Lanka.
    
    Logistics Data payload from Agent 1:
    {json.dumps(logistics_data, indent=2)}
    
    User Constraints:
    - Duration: {user_days} Days
    - Max Budget limit: {user_budget} LKR
    - Preferred Accommodation Tier: {accommodation_tier}
    
    Instructions:
    1. **Self-Reflection & Budget Verification**:
       - Calculate estimated entrance fees + accommodation ({accommodation_tier}) + transport.
       - Verify if the total fits strictly within {user_budget} LKR.
       - If it exceeds, adjust: swap out expensive destinations or luxury stays with affordable options (e.g. Galle Fort, beaches, free hikes like Little Adam's Peak, Hela Bojun meals).
    
    2. **Day-by-Day Detailed Itinerary**:
       - Morning, Afternoon, Evening breakdown for each day.
       - Recommend specific accommodations for each night matching the user's tier ({accommodation_tier}).
    
    3. **Essential Guidelines & Practical Traveler Guide**:
       Include dedicated sections for:
       - 🚨 **Emergency Hotlines & Safety**: Tourist Police (1912), 1990 Suwa Seriya Ambulance, Disaster Management (117), Regional Hospitals.
       - 🚗 **Transport & App Hacks**: PickMe/Uber coverage zones, Makumbura Highway Expressways, AAC Driving Permit rules for self-drive.
       - 🥗 **Authentic Dining & Hela Bojun Outlets**: Recommended Hela Bojun Hala outlets for healthy, budget vegetarian meals.
       - 📜 **Permits & Etiquette Guidelines**: DWC online permit portal (`dwc.lankagate.gov.lk`), temple dress codes, drone authorization rules.
    
    Output Format:
    Return clean, beautiful Markdown with clear headings, bullet points, and emojis.
    """
    
    reasoning_llm = get_reasoning_architect_llm()
    response = reasoning_llm.invoke(prompt)
    return response.content
