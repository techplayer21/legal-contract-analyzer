import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Groq is OpenAI-compatible! Use your free key from console.groq.com
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_clause(text_chunk: str):
    """
    Uses Llama 3.3 on Groq to provide stable, structured JSON analysis.
    """
    prompt = f"""
    Analyze this legal text for risks. 
    You MUST return a JSON object with exactly these keys: "clause_text", "risk_level", "issue", "suggested_edit".
    
    Text: {text_chunk}
    """
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a legal expert. Output ONLY valid JSON."},
                {"role": "user", "content": prompt}
            ],
            # This forces the model to output a valid JSON object
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        # Fallback to prevent the KeyError: 'risk_level' in main.py
        return {
            "clause_text": text_chunk[:100],
            "risk_level": "Error",
            "issue": f"Analysis failed: {str(e)}",
            "suggested_edit": "Check API key and try again."
        }