from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"E:\Tesseract-OCR\tesseract.exe" # Windows uchun (agar kerak bo‘lsa)

def extract_text(image):
    return pytesseract.image_to_string(image)