import re

def extract_invoice_data(text):
    data = {}

    # Invoice number
    invoice_no = re.search(r"(Invoice\s*#?\s*:?\s*)(\d+)", text, re.IGNORECASE)
    if invoice_no:
        data["invoice_no"] = invoice_no.group(2)

    # Date
    date = re.search(r"(\d{2}/\d{2}/\d{4})", text)
    if date:
        data["date"] = date.group(1)

    # Total amount
    total = re.search(r"(Total\s*:?\s*\$?\s*)(\d+\.?\d*)", text, re.IGNORECASE)
    if total:
        data["total"] = total.group(2)

    return data