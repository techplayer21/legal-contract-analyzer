# legal-contract-analyzer

### ⚖️ Project Overview:
​The AI Legal Contract Analyzer is a high-speed NLP tool designed to automate the preliminary review of legal documents. It identifies predatory clauses, assesses liability risks, and suggests safer alternative phrasing to protect the user's interests.

### ​🛠️ Tech Stack & Development Environment
​Language: Python 3.11.
​-AI Framework: Groq SDK for near-instant inference.
​-Frontend: Streamlit for a reactive web interface.
​-PDF Processing: PyMuPDF4LLM for markdown-based text extraction.
​-Containerization: Docker & Docker Compose for environment parity.
​-Cloud Hosting: Streamlit Community Cloud.
​
### ​📂 Repository Structure:
legal-analyzer/
├── app/
│   ├── main.py                # Streamlit UI & entry point
│   ├── services/
│   │   ├── contract_analyzer.py  # Orchestration of analysis pipeline
│   │   └── llm_service.py        # Groq API integration
│   └── utils/
│       ├── pdf_loader.py         # PDF text extraction logic
│       └── text_chunker.py       # Text splitting for model context
├── data/
│   └── uploads/               # Temporary storage for uploaded PDFs
├── .env                       # Local API keys (Git-ignored)
├── .gitignore                 # Prevents sensitive file uploads
├── Dockerfile                 # Python 3.11-slim build instructions
├── docker-compose.yml         # Container networking & volumes
└── requirements.txt           # Dependency manifest

### 🤖 Model Information:
​-Primary Model: Llama 3.3 (70B Versatile).
​-Inference Provider: Groq Cloud (LPU technology).
​-Optimization: Forced JSON Mode for stable data parsing and UI reliability.
​-Context: Optimized for processing large legal text chunks without loss of coherence.
​
### 🚀 Key Features:
​-Real-time Risk Scoring: Categorizes issues as High, Medium, or Low risk.
​-Legal Alternatives: Provides specific, safer rewrites for problematic clauses.
​Cloud-Secure Secrets: Uses Streamlit Secrets for encrypted API key management.
​Defensive Parsing: Implements .get() methods to prevent UI crashes on incomplete AI data.
​Container-Ready: Fully Dockerized for "plug-and-play" deployment.
