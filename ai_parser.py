from openai import OpenAI
import streamlit
import json

client = OpenAI(api_key=streamlit.secrets["OPENAI_API_KEY"])

def extract_with_gpt(text):
    prompt = f"""
You are an invoice data extractor.

Extract structured data from this invoice text.

Return ONLY JSON in this format:
{{
  "invoice_no": "",
  "date": "",
  "total": "",
  "currency": "",
  "vendor": "",
  "email": "",
  "phone_number": ""
}}

If something is missing, return null.

Invoice text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    result = response.choices[0].message.content

    try:
        return json.loads(result)
    except:
        return {"error": "Invalid JSON from GPT", "raw": result}
    
if __name__ == "__main__":
    sample_text = """
    Invoice No: INV-12345
    Date: 2026-04-01
    Vendor: ABC Company
    Total: 150.00 USD
    """

    result = extract_with_gpt(sample_text)
    print(result)