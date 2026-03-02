import sys
import os
import streamlit as st

# 1. CLOUD DEPLOYMENT FIX: 
# Adds the root directory of your project to the Python path so Streamlit can find 'app'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now you can safely import from your internal service modules
from app.services.contract_analyzer import run_full_analysis

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Legal Contract Analyzer", 
    page_icon="⚖️", 
    layout="wide"
)

# --- SIDEBAR ---
with st.sidebar:
    st.title("Settings & Info")
    st.markdown("---")
    st.info("This tool uses Llama 3.3 via Groq to analyze PDF contracts for predatory clauses and liability risks.")
    st.markdown("---")
    st.caption("Developed by Yash Raj")

# --- MAIN UI ---
st.title("⚖️ AI Legal Contract Analyzer")
st.write("Upload an architectural or startup contract (PDF) to identify high-risk clauses and liability issues.")

# File Uploader
uploaded_file = st.file_uploader("Upload Contract (PDF)", type=["pdf"])

if uploaded_file is not None:
    # Ensure the uploads directory exists
    temp_dir = os.path.join("data", "uploads")
    os.makedirs(temp_dir, exist_ok=True)
    
    # Save the file temporarily for processing
    temp_path = os.path.join(temp_dir, uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Analysis Button
    if st.button("Run Risk Analysis"):
        with st.spinner("Analyzing your contract..."):
            try:
                # Trigger the full analysis pipeline
                risks = run_full_analysis(temp_path)
                
                st.subheader("🚩 Risk Report")
                
                if not risks:
                    st.success("No significant legal risks identified in this document.")
                else:
                    # Loop through the results and display them in organized expanders
                    for risk in risks:
                        # Defensive coding: using .get() to prevent KeyError crashes
                        risk_lvl = risk.get('risk_level', 'Unknown')
                        
                        # Color coding based on risk severity
                        if risk_lvl == "High":
                            icon = "🔴"
                        elif risk_lvl == "Medium":
                            icon = "🟡"
                        else:
                            icon = "🔵"
                        
                        with st.expander(f"{icon} {risk_lvl} Risk: {risk.get('issue', 'Legal Detail')}"):
                            st.markdown(f"**Original Clause Text:**\n> {risk.get('clause_text', 'No text found.')}")
                            st.markdown(f"**Analysis & Issue:**\n{risk.get('issue', 'N/A')}")
                            st.markdown(f"**Suggested Safer Edit:**\n`{risk.get('suggested_edit', 'No edit suggested.')}`")
                            
            except Exception as e:
                st.error(f"Analysis Error: {str(e)}")
                st.info("Ensure your GROQ_API_KEY is correctly set in Streamlit Secrets.")

# --- FOOTER ---
st.markdown("---")
st.caption("Disclaimer: This tool is for preliminary review only. Always consult a qualified legal professional.")