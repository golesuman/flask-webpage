from PIL import Image
import pytesseract


def core_ocr(file):
    text=pytesseract.image_to_string(Image.open(file))
    return text