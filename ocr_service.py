import requests
from io import BytesIO

def image_to_bytes(image):
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()

def extract_text(image_bytes):
    url = "https://api.ocr.space/parse/image"

    response = requests.post(
        url,
        files={"file": ("image.png", image_bytes)},
        data={
            "apikey": "K82235285288957",
            "language": "eng"
        }
    )

    result = response.json()

    if result.get("IsErroredOnProcessing"):
        return {"error": result.get("ErrorMessage")}
    return result["ParsedResults"][0]["ParsedText"]

if __name__ == "__main__":
    with open("keraksiz3.png", "rb") as f:
        image_bytes = f.read()

    text = extract_text(image_bytes)
    print(text)