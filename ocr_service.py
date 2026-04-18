import requests

def extract_text(image_bytes):
    url = "https://api.ocr.space/parse/image"

    response = requests.post(
        url,
        files={"file": image_bytes},
        data={
            "apikey": "K82235285288957",
            "language": "eng"
        }
    )

    result = response.json()
    return result["ParsedResults"][0]["ParsedText"]