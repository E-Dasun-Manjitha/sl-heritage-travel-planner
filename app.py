import os
import streamlit as st
from agents import agent_1_logistics_specialist, agent_2_itinerary_architect

# 1. Page Configuration & Theme
st.set_page_config(
    page_title="Sri Lanka Tourist & Heritage Route Planner",
    page_icon="🇱🇰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Premium Custom CSS for Aesthetics
st.markdown("""
<style>
    /* Main Background & Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Elegant Sidebar styling */
    .css-1d391kg {
        background-color: #f7f9fb;
    }
    
    /* Title & Headers styling */
    h1 {
        font-weight: 800;
        color: #1e293b;
        background: linear-gradient(135deg, #FF9900 0%, #006400 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    
    /* Styled buttons */
    .stButton>button {
        background: linear-gradient(135deg, #FF9900 0%, #FFCC00 100%) !important;
        color: #1e293b !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15) !important;
        color: #000 !important;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        font-size: 16px;
        font-weight: 600;
        color: #64748b;
    }
    .stTabs [aria-selected="true"] {
        color: #FF9900 !important;
        border-bottom-color: #FF9900 !important;
    }
    
    /* Card Container */
    .travel-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 12px;
        border-left: 5px solid #FF9900;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 2. Main Header
st.markdown("""
<div style="display: flex; align-items: center; gap: 15px; margin-bottom: 10px;">
    <span style="font-size: 45px;">🇱🇰</span>
    <h1 style="margin: 0; padding: 0;">Sri Lanka Tourist & Heritage Route Planner</h1>
</div>
""", unsafe_allow_html=True)
st.markdown("An intelligent, agentic RAG assistant powered by **Llama 3.1 (Groq)** and **GPT-4o-mini (OpenRouter)** to craft optimized itineraries respecting budget constraints and temple dress codes.")

# 3. Sidebar inputs
st.sidebar.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <span style="font-size: 50px;">🗺️</span>
    <h3 style="margin-top: 5px; color: #1e293b;">Trip Planner</h3>
</div>
""", unsafe_allow_html=True)

st.sidebar.header("📋 Configure Parameters")

days = st.sidebar.slider("Trip Duration (Days)", min_value=1, max_value=7, value=3)

budget = st.sidebar.number_input("Total Budget (LKR)", min_value=10000, max_value=2000000, value=120000, step=5000, help="Specify total budget including accommodation, transportation, and entry tickets.")

accommodation_tier = st.sidebar.selectbox(
    "Select Accommodation Preference",
    ["Budget (Hostels & Homestays)", "Mid-Range (Villas & Eco Resorts)", "Luxury (5-Star & Plantation Estates)"],
    index=1
)

interests = st.sidebar.multiselect(
    "Select Travel Preferences",
    [
        "Culture & Heritage",
        "Nature & Wildlife",
        "Beaches & Surfing",
        "Food & Tea",
        "Adventure & Hiking",
        "Luxury & Wellness Retreats",
        "Budget & Backpacking",
        "Emergency & Safety Guidelines"
    ],
    default=["Culture & Heritage", "Nature & Wildlife"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Agent Architecture:**
- **Agent 1 (Groq / Llama 3.1):** RAG Fact Extractor (Queries 100-Doc Vector Store)
- **Agent 2 (OpenRouter / GPT-4o-mini):** Itinerary Architect (with budget self-reflection & safety guidelines)
""")

# 4. API Key Check warnings
groq_configured = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
openrouter_configured = st.secrets.get("OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")

if not groq_configured or not openrouter_configured:
    st.warning("⚠️ **API Keys Missing:** Please configure your API keys to enable LLM generation.")
    with st.expander("🔑 How to set up API Keys"):
        st.markdown("""
        To run the agents, open `.streamlit/secrets.toml` in your root folder and paste your keys:
        ```toml
        GROQ_API_KEY = "your_actual_groq_api_key_here"
        OPENROUTER_API_KEY = "your_actual_openrouter_api_key_here"
        ```
        Alternatively, you can export them as environment variables:
        ```bash
        export GROQ_API_KEY="gsk_..."
        export OPENROUTER_API_KEY="sk-or-..."
        ```
        """)

# 5. Planning Trigger
if st.sidebar.button("🚀 Generate Itinerary"):
    if not interests:
        st.error("Please select at least one travel preference.")
    else:
        # Check API key configurations
        try:
            selected_interests_str = ", ".join(interests)
            
            # Create progress bars and spinners
            with st.spinner("🤖 Agent 1: Retrieving tourist database facts (ChromaDB) and compiling logistics..."):
                extracted_facts, retrieved_docs = agent_1_logistics_specialist(selected_interests_str, days, accommodation_tier)
            
            with st.spinner("🧠 Agent 2: Synthesizing day-by-day planner and validating budget limits..."):
                final_itinerary = agent_2_itinerary_architect(extracted_facts, budget, days, accommodation_tier)
                
            st.success("✨ Your Sri Lankan travel plan has been compiled!")
            
            # Setup Tabs for display
            tab1, tab2 = st.tabs(["🗺️ Day-by-Day Itinerary", "🔍 RAG Verification & Source Chunks"])
            
            with tab1:
                st.markdown(final_itinerary)
                
            with tab2:
                st.subheader("Retrieved Context Chunks (Ground Truth Sources)")
                st.write(f"The vector database retrieved {len(retrieved_docs)} matching documents to ground the agents' knowledge base:")
                for idx, doc in enumerate(retrieved_docs):
                    source_name = doc.metadata.get('source', 'Unknown source')
                    source_basename = os.path.basename(source_name)
                    with st.expander(f"📄 Chunk {idx+1} — {source_basename}"):
                        st.markdown(f"**Source File:** `{source_name}`")
                        st.info(doc.page_content)
                        
        except Exception as e:
            st.error("An error occurred during generation.")
            st.exception(e)
