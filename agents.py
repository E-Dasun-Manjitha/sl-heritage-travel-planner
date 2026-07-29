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
    if groq_key and groq_key != "your_actual_groq_api_key_here":
        try:
            return ChatGroq(
                model_name="llama-3.1-8b-instant",
                groq_api_key=groq_key,
                temperature=0.2,
                max_retries=2
            )
        except Exception:
            pass
    return ChatOpenAI(
        model_name="openai/gpt-4o-mini",
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=openrouter_key,
        temperature=0.2,
        max_retries=3
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

# 3. Vector Database Connection (Auto-builds if missing on Streamlit Cloud)
@st.cache_resource
def get_vector_db():
    if not os.path.exists("./chroma_db") or not os.listdir("./chroma_db"):
        from rag_builder import build_vector_database
        build_vector_database()
        
    def _init_embeddings():
        for attempt in range(4):
            try:
                return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
            except Exception:
                import time
                time.sleep(1.5)
        return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    embeddings = _init_embeddings()
    return Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

def agent_1_logistics_specialist(user_interests, user_days, accommodation_tier="Mid-Range"):
    """
    Agent 1 (Tool-Use & Router Pattern):
    Queries the vector DB for attractions, accommodation, adventure packages, emergency hotlines, transport, and dining.
    Structures a comprehensive, highly detailed logistics JSON payload for Agent 2.
    """
    vector_db = get_vector_db()
    if vector_db is None:
        return json.dumps({"error": "Vector database initialization failed."}), []
        
    # Construct targeted search query combining interests, accommodation tier, and essential rules (Router Pattern)
    query = f"Attractions, entrance ticket fees, {accommodation_tier} accommodation, transport apps, expressway bus terminals, emergency tourist police hotlines, hospitals, Hela Bojun dining outlets, permits, and temple dress codes for {user_interests} in {user_days} days"
    
    # Retrieve top 15 matching document chunks across the 100-document knowledge base (Tool-Use Pattern)
    retrieved_docs = vector_db.similarity_search(query, k=15)
    context_text = "\n\n".join([f"Source {i+1} ({doc.metadata.get('source', 'Unknown')}):\n{doc.page_content}" for i, doc in enumerate(retrieved_docs)])
    
    prompt = f"""
    You are Agent 1 (Logistics Specialist).
    Your task is to review the retrieved tourist facts and organize them into a comprehensive, highly detailed structured JSON payload for the Itinerary Architect.
    
    Retrieved Context:
    {context_text}
    
    User Parameters:
    - Interests: {user_interests}
    - Days: {user_days}
    - Preferred Accommodation Tier: {accommodation_tier}
    
    Instructions:
    Extract facts strictly from the context above. Group them into detailed JSON fields:
    1. attractions (name, location/city, fee in LKR or USD, dress code, opening rules, key sights, recommended duration)
    2. accommodation_options (tier, location, price range, recommended places, key amenities)
    3. transport_and_apps (ride-hailing coverage, PickMe/Uber intercity fares, expressways, train booking, driving permits)
    4. emergency_and_police_hotlines (tourist police 1912 & regional units, ambulance 1990, disaster 117, hospitals)
    5. dining_and_hela_bojun (Hela Bojun outlets & menu prices, local food costs, specialties)
    6. permits_and_safety_rules (temple etiquettes, DWC online permits, Forest Dept permits, drone rules)
    
    You MUST respond ONLY with a valid JSON block containing:
    {{
      "attractions": [
        {{"name": "...", "location": "...", "fee": "...", "rules": "...", "details": "..."}}
      ],
      "accommodation_options": [
        {{"tier": "...", "location": "...", "price_range": "...", "options": "...", "amenities": "..."}}
      ],
      "transport_and_apps": [
        {{"service": "...", "details": "...", "costs": "..."}}
      ],
      "emergency_and_police_hotlines": [
        {{"facility": "...", "contact": "...", "role": "..."}}
      ],
      "dining_and_hela_bojun": [
        {{"outlet": "...", "details": "...", "price_range": "..."}}
      ],
      "permits_and_safety_rules": ["..."]
    }}
    Do not add any conversational text before or after the JSON.
    """
    
    response = None
    for attempt in range(3):
        try:
            fast_llm = ChatGroq(model_name="llama-3.1-8b-instant", groq_api_key=groq_key, temperature=0.2, request_timeout=25.0)
            response = fast_llm.invoke(prompt)
            break
        except Exception:
            try:
                fast_llm = ChatOpenAI(model_name="openai/gpt-4o-mini", openai_api_base="https://openrouter.ai/api/v1", openai_api_key=openrouter_key, temperature=0.2, request_timeout=30.0)
                response = fast_llm.invoke(prompt)
                break
            except Exception as e:
                if attempt == 2:
                    raise e
                import time
                time.sleep(2)
            
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
    Receives structured output from Agent 1 and builds a deeply descriptive, day-by-day plan adhering to constraints.
    Performs a reflection loop checking the total budget (fees + accommodation + transport + dining).
    Appends full guidelines (emergency hotlines, transport hacks, Hela Bojun dining, and permits).
    """
    # Parse the logistics payload (Agent-to-Agent communication)
    try:
        logistics_data = json.loads(extracted_logistics_json)
    except Exception:
        logistics_data = {"error": "Could not parse JSON payload from Agent 1", "raw": extracted_logistics_json}
        
    prompt = f"""
    You are Agent 2 (Itinerary Architect & Master Travel Guide for Sri Lanka).
    You will create a deeply descriptive, rich, comprehensive, and high-value {user_days}-Day Complete Travel Itinerary & Guidelines for Sri Lanka.
    
    Logistics Data payload from Agent 1:
    {json.dumps(logistics_data, indent=2)}
    
    User Constraints:
    - Trip Duration: {user_days} Days
    - Max Budget limit: {user_budget:,} LKR
    - Preferred Accommodation Tier: {accommodation_tier}
    
    CRITICAL INSTRUCTIONS FOR MAXIMUM DETAIL & DESCRIPTIVENESS:
    1. **Self-Reflection & Budget Verification**:
       - Calculate estimated entrance fees + accommodation for {user_days} nights ({accommodation_tier}) + transport + food.
       - Verify if the total fits strictly within {user_budget:,} LKR.
       - If it exceeds, perform a reflection adjustment: swap out expensive private tours or high-tier stays for affordable alternatives (e.g. Galle Fort strolls, public/express transport, Hela Bojun meals, free hikes). Explicitly document this budget validation in the text.
    
    2. **Executive Overview & Route Strategy**:
       - Provide a concise text overview of the travel route theme, major highlights, and target locations (Do NOT include a budget table here).
    
    3. **Deeply Detailed Day-by-Day Itinerary**:
       Provide a rich, immersive breakdown for EVERY SINGLE DAY from Day 1 to Day {user_days}.
       For each day, structure into:
       - 🌅 **Morning (07:00 AM - 12:00 PM)**:
         - **Sightseeing & Experience**: Descriptive narrative of historical context, architecture, key features, and recommended duration.
         - **Transit & Route**: Exact mode of transport (e.g., train, PickMe, metered tuk-tuk, express bus), estimated travel time, route directions, estimated transport cost.
         - **Culinary Highlight**: Recommended breakfast dishes (e.g., egg hoppers, string hoppers, Ceylon tea) and venue/cost.
         - **Entrance & Fees**: Exact ticket price in LKR/USD and purchase location.
         - **Insider Tips & Etiquette**: Dress code rules (e.g., shoulders & knees covered, shoes off), best camera angles, crowd avoidance.
       - ☀️ **Afternoon (12:00 PM - 05:00 PM)**:
         - Complete descriptive narrative for afternoon activities, transport details, recommended lunch (e.g., local rice & curry or Hela Bojun outlet), entry costs, and practical rules.
       - 🌙 **Evening & Night (05:00 PM - 10:00 PM)**:
         - Evening sunset spot, relaxing walk, night market/dining recommendations, and dinner budget.
       - 🏨 **Nightly Accommodation**:
         - Specific hotel/stay recommendation matching the user's accommodation tier ({accommodation_tier}), area location, key amenities, and estimated rate per night.
    
    4. **Itemized Financial & Budget Summary Table**:
       (IMPORTANT: This must be the ONLY budget table in the entire response. Do NOT create any other budget tables.)
       Provide a single clean Markdown table summarizing:
       | Expense Category | Details | Estimated Cost (LKR) |
       | --- | --- | --- |
       | Entrance Fees & Permits | All attractions | ... |
       | Accommodation ({user_days} Nights) | {accommodation_tier} stays | ... |
       | Transportation & Transit | Trains, tuk-tuks, buses, taxis | ... |
       | Meals & Dining | Breakfast, Hela Bojun lunches, dinners | ... |
       | Emergency Contingency Reserve | 10% safety buffer | ... |
       | **GRAND TOTAL ESTIMATED COST** | | **... LKR** |
       | **USER BUDGET LIMIT** | | **{user_budget:,} LKR** |
       - Add a clear validation note: `✅ Validated within user budget constraint` or budget adjustment explanation.
    
    5. **Essential Guidelines & Practical Traveler Guide**:
       Include comprehensive, actionable sections for:
       - 🚨 **Emergency Hotlines & Medical Care**: Tourist Police (1912 & regional units: Kandy, Galle, Sigiriya), Ambulance (1990 Suwa Seriya), Disaster Management (117), National Hospital Colombo (+94 11 269 1111), Kandy Teaching Hospital, Karapitiya Galle Hospital.
       - 🚗 **Transport Hacks & App Logistics**: PickMe & Uber coverage zones, Makumbura Highway Expressways, 30-day train seat reservation rules (`seatreservation.railway.gov.lk`), AAC International Driving Permit endorsement rules in Colombo.
       - 🥗 **Authentic Dining & Hela Bojun Outlets**: Detailed Hela Bojun Hala guide (locations: Peradeniya, Dambulla, Battaramulla, Matara), recommended items (Kurakkan pittu, polos cutlets, Ranawara herbal tea) and prices (LKR 50-300).
       - 📜 **Permits, Etiquette & Cultural Rules**: DWC online permit portal (`dwc.lankagate.gov.lk`), Forest Dept camping rules, strict temple dress codes (shoulders/knees covered, no Buddha tattoos/posing back to Buddha), Civil Aviation drone permits.
    
    Output Format:
    Return clean, beautiful, highly descriptive Markdown with clear headers (`#`, `##`, `###`), bold text, callout emojis, bullet points, and EXACTLY ONE budget table.
    """
    
    reasoning_llm = get_reasoning_architect_llm()
    response = None
    for attempt in range(4):
        try:
            response = reasoning_llm.invoke(prompt)
            break
        except Exception as e:
            if attempt == 3:
                raise e
            import time
            time.sleep(2)
            
    return response.content

