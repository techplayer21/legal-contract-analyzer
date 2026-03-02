import pymupdf4llm

def load_and_convert_pdf(file_path):
    try:
        md_text = pymupdf4llm.to_markdown(file_path)
        return md_text
    except Exception as e:
        return f"Error loading PDF: {str(e)}"