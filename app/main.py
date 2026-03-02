import streamlit as st
import os
from app.services.contract_analyzer import run_full_analysis

st.set_page_config(page_title="AI Legal Contract Analyzer", layout="wide")

st.title("⚖️ AI Legal Contract Analyzer")
st.subheader("Upload a contract to flag risky clauses and get suggested edits.")

uploaded_file = st.file_uploader("Upload Contract (PDF)", type=["pdf"])

if uploaded_file is not None:
    # Save the file temporarily
    temp_path = os.path.join("data/uploads", uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File '{uploaded_file.name}' uploaded successfully!")
    
    if st.button("Analyze Contract"):
        with st.spinner("Analyzing legal language... this may take a moment."):
            # Run the backend logic
            results = run_full_analysis(temp_path)
            
            # Display results
            st.write("### 🚩 Risk Report")
            for risk in results:
                with st.expander(f"Risk Level: {risk.get('risk_level', 'unknown')}"):
                    st.markdown(f"**Original Clause:** {risk['clause_text']}")
                    st.error(f"**Issue:** {risk['issue']}")
                    st.info(f"**Suggested Edit:** {risk['suggested_edit']}")