import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\PC.01\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image
img = Image.open('c.png')
text = tess.image_to_string(img)
print(text)