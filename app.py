import os
import json
import math
import pandas as pd
import pydeck as pdk
import streamlit as st
from agents import agent_1_logistics_specialist, agent_2_itinerary_architect

# Location Coordinate Database for Sri Lanka Destinations
SRI_LANKA_COORDINATES = {
    "sigiriya": {"lat": 7.9570, "lon": 80.7603, "name": "Sigiriya", "type": "Heritage Site"},
    "dambulla": {"lat": 7.8742, "lon": 80.6511, "name": "Dambulla", "type": "Sacred Temple"},
    "polonnaruwa": {"lat": 7.9403, "lon": 81.0188, "name": "Polonnaruwa", "type": "Archaeological Park"},
    "anuradhapura": {"lat": 8.3114, "lon": 80.4037, "name": "Anuradhapura", "type": "Ancient Stupas"},
    "kandy": {"lat": 7.2906, "lon": 80.6337, "name": "Kandy", "type": "Sacred Shrine"},
    "galle": {"lat": 6.0535, "lon": 80.2210, "name": "Galle", "type": "Living Heritage"},
    "yala": {"lat": 6.3725, "lon": 81.5165, "name": "Yala", "type": "Wildlife Safari"},
    "sinharaja": {"lat": 6.4167, "lon": 80.4167, "name": "Sinharaja", "type": "UNESCO Rainforest"},
    "ella": {"lat": 6.8667, "lon": 81.0466, "name": "Ella", "type": "Scenic Hiking"},
    "mirissa": {"lat": 5.9483, "lon": 80.4716, "name": "Mirissa", "type": "Beach & Wildlife"},
    "hikkaduwa": {"lat": 6.1394, "lon": 80.1063, "name": "Hikkaduwa", "type": "Marine Sanctuary"},
    "colombo": {"lat": 6.9271, "lon": 79.8612, "name": "Colombo ✈️", "type": "Capital & Airport"},
    "horton plains": {"lat": 6.8028, "lon": 80.8091, "name": "Horton Plains", "type": "National Park"},
    "nuwara eliya": {"lat": 6.9497, "lon": 80.7891, "name": "Nuwara Eliya", "type": "Hill Country"},
    "adam's peak": {"lat": 6.8096, "lon": 80.4994, "name": "Adam's Peak", "type": "Pilgrimage Mountain"},
    "pinnawala": {"lat": 7.3013, "lon": 80.3846, "name": "Pinnawala", "type": "Elephant Sanctuary"},
    "bentota": {"lat": 6.4225, "lon": 79.9984, "name": "Bentota", "type": "Water Sports"},
    "jaffna": {"lat": 9.6615, "lon": 80.0255, "name": "Jaffna", "type": "Northern Heritage"},
    "trincomalee": {"lat": 8.5874, "lon": 81.2152, "name": "Trincomalee", "type": "Marine & Temple"},
    "arugam bay": {"lat": 6.8415, "lon": 81.8358, "name": "Arugam Bay", "type": "Surfing Bay"},
    "udawalawe": {"lat": 6.4746, "lon": 80.8987, "name": "Udawalawe", "type": "Elephant Safari"},
    "kitulgala": {"lat": 6.9904, "lon": 80.4132, "name": "Kitulgala", "type": "Adventure Sports"},
    "knuckles": {"lat": 7.4475, "lon": 80.7786, "name": "Knuckles", "type": "Mountain Trekking"},
    "weligama": {"lat": 5.9734, "lon": 80.4287, "name": "Weligama", "type": "Surf School"},
    "tangalle": {"lat": 6.0244, "lon": 80.7941, "name": "Tangalle", "type": "Ocean Resort"},
    "negombo": {"lat": 7.2008, "lon": 79.8737, "name": "Negombo", "type": "Beach & Lagoon"},
    "tissa": {"lat": 6.2842, "lon": 81.2847, "name": "Tissa", "type": "Safari Base"},
    "tissamaharama": {"lat": 6.2842, "lon": 81.2847, "name": "Tissa", "type": "Safari Base"},
    "hatton": {"lat": 6.8916, "lon": 80.5956, "name": "Hatton", "type": "Tea Estate"}
}

def extract_locations_dataframe(itinerary_text, logistics_json_str):
    """
    Parses the generated itinerary text and logistics payload to extract locations
    in exact chronological travel sequence from Day 1 to Day N.
    """
    locations_list = []
    seen_names = set()
    
    # Scan text prioritizing itinerary_text for chronological day-by-day order
    text_to_scan = (itinerary_text or "") + "\n" + (logistics_json_str or "")
    text_lower = text_to_scan.lower()
    
    # Find positions of all matched locations in the itinerary text
    found_matches = []
    for key, coord in SRI_LANKA_COORDINATES.items():
        pos = text_lower.find(key)
        if pos != -1:
            found_matches.append((pos, key, coord))
            
    # Sort locations by their appearance order in the itinerary text to preserve Day 1 -> Day N sequence
    found_matches.sort(key=lambda x: x[0])
    
    for pos, key, coord in found_matches:
        if coord["name"] not in seen_names:
            seen_names.add(coord["name"])
            locations_list.append({
                "name": coord["name"],
                "lat": coord["lat"],
                "lon": coord["lon"],
                "type": coord["type"],
                "details": f"Suggested Stop along Day-by-Day Route"
            })
            
    # Fallback default loop if empty
    if not locations_list:
        locations_list = [
            {"name": "Colombo ✈️", "lat": 6.9271, "lon": 79.8612, "type": "Gateway", "details": "Capital City & Airport"},
            {"name": "Dambulla", "lat": 7.8742, "lon": 80.6511, "type": "Sacred Temple", "details": "Cave Temple"},
            {"name": "Sigiriya", "lat": 7.9570, "lon": 80.7603, "type": "Ancient Rock", "details": "Lion Rock Fortress"},
            {"name": "Kandy", "lat": 7.2906, "lon": 80.6337, "type": "Heritage", "details": "Temple of Tooth Relic"},
            {"name": "Nuwara Eliya", "lat": 6.9497, "lon": 80.7891, "type": "Tea Country", "details": "Tea Estate Scenery"},
            {"name": "Ella", "lat": 6.8667, "lon": 81.0466, "type": "Mountains", "details": "Nine Arch Bridge & Hikes"},
            {"name": "Yala", "lat": 6.3725, "lon": 81.5165, "type": "Safari", "details": "Leopard Safari Park"},
            {"name": "Galle", "lat": 6.0535, "lon": 80.2210, "type": "Living Fort", "details": "Dutch Ramparts"},
            {"name": "Bentota", "lat": 6.4225, "lon": 79.9984, "type": "Beach", "details": "Golden Sands"}
        ]
        
    # Add sequence numbers and map labels
    circled_nums = ["①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨", "⑩", "⑪", "⑫", "⑬", "⑭", "⑮"]
    for idx, item in enumerate(locations_list):
        num_str = circled_nums[idx] if idx < len(circled_nums) else f"({idx+1})"
        item["stop_number"] = idx + 1
        item["map_label"] = f"{num_str} {item['name']}"
        
    df = pd.DataFrame(locations_list)
    return df

def compute_route_arrows(df):
    """Computes midpoint coordinates and bearing angle for directional red arrows along the route."""
    arrows = []
    for i in range(len(df) - 1):
        p1 = df.iloc[i]
        p2 = df.iloc[i+1]
        
        # Position arrow at 55% along the leg
        mid_lat = p1['lat'] * 0.45 + p2['lat'] * 0.55
        mid_lon = p1['lon'] * 0.45 + p2['lon'] * 0.55
        
        # Bearing calculation in spherical coordinates
        d_lon = (p2['lon'] - p1['lon']) * math.cos(math.radians((p1['lat'] + p2['lat'])/2))
        d_lat = p2['lat'] - p1['lat']
        angle = math.degrees(math.atan2(d_lon, d_lat))
        
        arrows.append({
            "lat": mid_lat,
            "lon": mid_lon,
            "angle": -angle,  # PyDeck rotation
            "symbol": "▲"
        })
    return pd.DataFrame(arrows)

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
    
    /* Table styling for financial & summary tables */
    table {
        width: 100% !important;
        border-collapse: collapse !important;
        margin: 15px 0 !important;
    }
    th {
        background-color: #f1f5f9 !important;
        color: #1e293b !important;
        font-weight: 700 !important;
        padding: 10px 14px !important;
        border: 1px solid #cbd5e1 !important;
        text-align: left !important;
    }
    td {
        padding: 10px 14px !important;
        border: 1px solid #e2e8f0 !important;
    }
    tr:nth-child(even) {
        background-color: #f8fafc !important;
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
            
            # Extract DataFrame of places in chronological travel order
            map_df = extract_locations_dataframe(final_itinerary, extracted_facts)
            
            # Setup Tabs for display
            tab1, tab2, tab3 = st.tabs(["🗺️ Day-by-Day Itinerary", "📍 Interactive Route Map", "🔍 RAG Verification & Source Chunks"])
            
            with tab1:
                st.markdown(final_itinerary)
                
            with tab2:
                st.subheader("📍 Sri Lanka Tourist Route & Destination Map")
                st.markdown(f"Topographic travel route map highlighting **{len(map_df)} destination stops** and travel directions across Sri Lanka:")
                
                # Compute directional arrows DataFrame
                arrows_df = compute_route_arrows(map_df)
                
                # Render PyDeck Interactive Map with CartoDB Voyager Topographic Style (Focused tightly on Sri Lanka)
                center_lat = float(map_df["lat"].mean()) if not map_df.empty else 7.75
                center_lon = float(map_df["lon"].mean()) if not map_df.empty else 80.70
                
                view_state = pdk.ViewState(
                    latitude=center_lat,
                    longitude=center_lon,
                    zoom=7.9,
                    pitch=0
                )
                
                # Red path line connecting destination stops
                path_data = [{"path": map_df[["lon", "lat"]].values.tolist()}]
                path_layer = pdk.Layer(
                    "PathLayer",
                    path_data,
                    get_path="path",
                    get_color="[220, 38, 38, 240]",
                    width_scale=20,
                    width_min_pixels=3,
                    pickable=False
                )
                
                # Directional red arrow markers along the route path
                arrows_layer = pdk.Layer(
                    "TextLayer",
                    arrows_df,
                    get_position=["lon", "lat"],
                    get_text="symbol",
                    get_angle="angle",
                    get_size=18,
                    get_color="[220, 38, 38, 255]",
                    get_text_anchor="'middle'",
                    get_alignment_baseline="'center'"
                )
                
                # Red circular destination pins with dark red borders (matching StepMap style)
                scatter_layer = pdk.Layer(
                    "ScatterplotLayer",
                    map_df,
                    get_position=["lon", "lat"],
                    get_fill_color="[220, 38, 38, 255]",
                    get_line_color="[153, 27, 27, 255]",
                    line_width_min_pixels=2,
                    get_radius=8500,
                    pickable=True,
                    auto_highlight=True
                )
                
                # Clean place text labels next to each destination pin
                text_layer = pdk.Layer(
                    "TextLayer",
                    map_df,
                    get_position=["lon", "lat"],
                    get_text="map_label",
                    get_size=15,
                    get_color="[15, 23, 42, 255]",
                    get_background_color="[255, 255, 255, 220]",
                    get_border_color="[220, 38, 38, 200]",
                    get_border_width=1,
                    padding=[3, 6],
                    get_text_anchor="'left'",
                    get_alignment_baseline="'center'"
                )
                
                deck = pdk.Deck(
                    layers=[path_layer, arrows_layer, scatter_layer, text_layer],
                    initial_view_state=view_state,
                    map_style="https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json",
                    tooltip={"text": "📍 Stop #{stop_number}: {name}\nCategory: {type}\n{details}"}
                )
                
                st.pydeck_chart(deck)
                
                st.markdown("---")
                st.markdown("### 📋 Suggested Destination Summary")
                st.dataframe(
                    map_df[["stop_number", "name", "type", "lat", "lon", "details"]],
                    column_config={
                        "stop_number": "Stop #",
                        "name": "Destination Name",
                        "type": "Category",
                        "lat": "Latitude",
                        "lon": "Longitude",
                        "details": "Details & Fee Notes"
                    },
                    use_container_width=True
                )
                
                # Google Maps Route Link
                gmaps_coords = "/".join([f"{row['lat']},{row['lon']}" for _, row in map_df.iterrows()])
                gmaps_url = f"https://www.google.com/maps/dir/{gmaps_coords}"
                st.markdown(f"👉 [**🌐 Open Complete Travel Route in Google Maps**]({gmaps_url})")
                
            with tab3:
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

