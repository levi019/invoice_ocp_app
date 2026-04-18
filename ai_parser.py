from openai import OpenAI
import json

client = OpenAI(api_key="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")

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
  "vendor": ""
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