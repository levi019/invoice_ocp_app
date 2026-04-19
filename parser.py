import re

def extract_invoice_data(text):
    data = {}

    # Invoice number
    invoice_no = re.search(r"Invoice\s*#?\s*:?\s*([A-Za-z0-9-]+)", text, re.IGNORECASE)
    if invoice_no:
        data["invoice_no"] = invoice_no.group(1)

    # Date
    date = re.search(r"(\d{2}/\d{2}/\d{4})", text)
    if date:
        data["date"] = date.group(1)

    # Total amount
    total = re.search(r"(Total\s*:?\s*\$?\s*)(\d+\.?\d*)", text, re.IGNORECASE)
    if total:
        data["total"] = total.group(2)

    # Email
    email = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    if email:
        data["email"] = email.group(0)

    # Vendor (oddiy variant)
    vendor = re.search(r"(Vendor\s*:?\s*)(.+)", text, re.IGNORECASE)
    if vendor:
        data["vendor"] = vendor.group(2).strip()

    return data

if __name__ == "__main__":
    sample_text = """
    Invoice #INV-1001
    Date: 04/19/2026
    Vendor: ABC Company LLC
    Email: info@abccompany.com
    Total: $320.50
    """

    result = extract_invoice_data(sample_text)
    print(result)