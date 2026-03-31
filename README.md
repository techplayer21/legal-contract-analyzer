# legal-contract-analyzer

### ⚖️ Project Overview:
​The AI Legal Contract Analyzer is a high-speed NLP tool designed to automate the preliminary review of legal documents. It identifies predatory clauses, assesses liability risks, and suggests safer alternative phrasing to protect the user's interests.

### ​🛠️ Tech Stack & Development Environment
​-Language: Python 3.11. <br>
​-AI Framework: Groq SDK for near-instant inference. <br>
​-Frontend: Streamlit for a reactive web interface. <br>
​-PDF Processing: PyMuPDF4LLM for markdown-based text extraction. <br>
​-Containerization: Docker & Docker Compose for environment parity. <br>
​-Cloud Hosting: Streamlit Community Cloud. <br>
​
### ​📂 Repository Structure:
legal-analyzer/ <br>
├── app/ <br>
│   ├── main.py <br>
│   ├── services/ <br>
│   │   ├── contract_analyzer.py <br>
│   │   └── llm_service.py <br>
│   └── utils/ <br>
│       ├── pdf_loader.py <br>
│       └── text_chunker.py <br>
├── data/ <br>
│   └── uploads/ <br>
├── .env                   
├── .gitignore            
├── Dockerfile            
├── docker-compose.yml         
└── requirements.txt          

### 🤖 Model Information:
​-Primary Model: Llama 3.3 (70B Versatile). <br>
​-Inference Provider: Groq Cloud (LPU technology). <br>
​-Optimization: Forced JSON Mode for stable data parsing and UI reliability. <br>
​-Context: Optimized for processing large legal text chunks without loss of coherence. <br>
​
### 🚀 Key Features:
​-Real-time Risk Scoring: Categorizes issues as High, Medium, or Low risk. <br>
​-Legal Alternatives: Provides specific, safer rewrites for problematic clauses. <br>
​Cloud-Secure Secrets: Uses Streamlit Secrets for encrypted API key management. <br>
​Defensive Parsing: Implements .get() methods to prevent UI crashes on incomplete AI data. <br>
​Container-Ready: Fully Dockerized for "plug-and-play" deployment. <br>
