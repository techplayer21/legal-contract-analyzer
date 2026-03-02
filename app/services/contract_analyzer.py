from app.utils.pdf_loader import load_and_convert_pdf
from app.utils.text_chunker import chunk_legal_text
from app.services.llm_service import analyze_clause

def run_full_analysis(file_path: str):
    raw_text = load_and_convert_pdf(file_path)
    chunks = chunk_legal_text(raw_text)

    risks = []
    # Let's just analyze the first 3 chunks to save your API credits for now
    for chunk in chunks[:3]:
        risk = analyze_clause(chunk)
        risks.append(risk)

    return risks