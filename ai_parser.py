from openai import OpenAI
import streamlit
import json

client = OpenAI(api_key=streamlit.secrets["OPENAI_API_KEY"])

def extract_with_gpt(text):
    prompt0 = f"""
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

    prompt1 = f"""
You are a strict invoice data extraction system.

Your task is to extract ONLY explicitly stated information from the invoice text.

Rules:
- Do NOT guess or infer missing values
- Do NOT fabricate data
- If a field is not clearly present, return null
- If NONE of the fields are found, return an empty JSON: {{}}
- Return ONLY valid JSON (no explanation, no text)

Extract the following fields:
- invoice_no
- date
- total
- currency
- vendor
- email
- phone_number

Output format:
{{
  "invoice_no": string or null,
  "date": string or null,
  "total": string or null,
  "currency": string or null,
  "vendor": string or null,
  "email": string or null,
  "phone_number": string or null
}}

Invoice text:
{text}
"""
    
    prompt3 = f"""
You are an intelligent information extraction system.

Your task is to extract ALL meaningful and structured information from the given text.

Rules:
- Extract only information explicitly present in the text
- Do NOT guess or infer
- Identify key-value pairs, entities, attributes, and facts
- Normalize keys into short, clear snake_case format
- Group related data when possible
- If no useful information is found, return {{}}
- Return ONLY valid JSON (no explanation)

Examples of what to extract:
- names
- locations
- dates
- numbers (prices, rewards, counts)
- objects
- events
- attributes (color, type, status, etc.)

Text:
{text}
"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt3}
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