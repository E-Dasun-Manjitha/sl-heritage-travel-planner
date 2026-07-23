# 🇱🇰 Sri Lanka Tourist & Heritage Route Planner (Agentic AI)

An intelligent, multi-agent, RAG-driven travel planner application that designs custom daily travel itineraries across Sri Lanka based on user budget, trip duration, and preferences.

🌐 **Live Streamlit App:** [Deploy on Streamlit Community Cloud](https://share.streamlit.io/)

---

## 🏗️ Architecture & Agent Flow

The application uses a custom multi-agent orchestration pattern where agents exchange structured payloads to refine recommendations.

```mermaid
sequenceDiagram
    autonumber
    actor User as User Interface (Streamlit)
    participant A1 as Agent 1: RAG Specialist (Llama 3.1)
    database DB as Vector Database (ChromaDB)
    participant A2 as Agent 2: Itinerary Architect (Claude 3.5)

    User->>A1: Request (Interests, Budget, Days)
    activate A1
    A1->>DB: Similarity Search query (Tool-Use)
    DB-->>A1: Relevant tourist & cost text chunks
    A1->>A1: Extract facts, fees & rules
    A1-->>A2: Structured JSON Payload (Facts & Fees)
    deactivate A1
    activate A2
    A2->>A2: Draft Initial Route Plan
    A2->>A2: Self-Reflection Loop: Sum costs and check vs budget
    Note over A2: Swaps expensive items if budget exceeded
    A2-->>User: Markdown Day-by-Day Itinerary & Cost Verification
    deactivate A2
```

---

## 🤖 Model Selection Strategy Comparison

| Sub-task | Selected Model & Provider | Justification |
| :--- | :--- | :--- |
| **Intent Routing & Context Extraction** | `llama-3.1-8b-instant` (via Groq) | Extremely low latency, near-zero cost, highly efficient for parsing user queries and extracting facts/JSON structures. |
| **Itinerary Synthesis & Budget Check** | `claude-3.5-sonnet` (via OpenRouter) | Superior reasoning, spatial awareness of Sri Lankan geography, strict compliance with complex layout constraints, and self-reflection logic. |

---

## 🛠️ Agentic Design Patterns Used

1. **Tool-Use Pattern:** Agent 1 queries the local Chroma vector database to fetch factual ticket fees, local transport rates, and rules from the knowledge base.
2. **Router Pattern:** Agent 1 parses selected user interest tags to create specialized search vectors.
3. **Reflection Pattern:** Agent 2 checks its own drafted schedule to ensure the total entrance fees and transport fit the user's budget ceiling. If they do not, it runs an adjusting loop to replace expensive items with affordable alternatives.

---

## 🧪 RAG Retrieval Quality Evaluation

The ingestion pipeline chunks 30 documents using a `RecursiveCharacterTextSplitter` (600 characters size, 100 overlap) and caches vectors using open-source `sentence-transformers/all-MiniLM-L6-v2`.

| Sample Query | Retrieved Context Relevant? | Commentary |
| :--- | :--- | :--- |
| *What is the entrance fee for Sigiriya?* | ✅ Yes | Correctly fetched $35 USD (~11,300 LKR) from `doc_01_sigiriya.txt`. |
| *What time does the train leave Kandy for Ella?* | ✅ Yes | Retrieved train booking costs (1st class reserved 3000-5000 LKR) from `doc_09_train_kandy_ella.txt`. |
| *What should I wear at Buddhist temples?* | ✅ Yes | Extracted rules requiring covering shoulders/knees and removing footwear from `doc_13_temple_dress_code.txt`. |
| *How much is a safari at Yala?* | ✅ Yes | Retrieved $30-$40 USD entry plus 12,000-18,000 LKR jeep rental from `doc_07_yala_national_park.txt`. |
| *What food costs should I expect in Sri Lanka?* | ✅ Yes | Extracted typical local breakfast (200-400 LKR) and kottu roti (600-1,200 LKR) from `doc_23_sri_lankan_food_costs.txt`. |

---

## ⚙️ Local Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/sl-heritage-travel-planner.git
   cd sl-heritage-travel-planner
   ```

2. **Set up Virtual Environment:**
   ```bash
   python -m venv venv
   # Activate:
   venv\Scripts\activate # Windows
   source venv/bin/activate # Mac/Linux
   ```

3. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Populate Database:**
   ```bash
   python generate_data.py
   python rag_builder.py
   ```

5. **Configure Secrets:**
   Create `.streamlit/secrets.toml`:
   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key_here"
   OPENROUTER_API_KEY = "your_actual_openrouter_api_key_here"
   ```

6. **Run Streamlit app:**
   ```bash
   streamlit run app.py
   ```
