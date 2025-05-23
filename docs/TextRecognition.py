import cv2
import deep_translator.exceptions
import pytesseract
from deep_translator import GoogleTranslator, single_detection
from Keys import detect_languages_api


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
img = cv2.imread('SpanishTextRecognition.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))

boxes = pytesseract.image_to_data(img)
hImg, wImg, _ = img.shape

for x, b in enumerate(boxes, splitlines()):
    if x != 0:
        b = b.split()
        # print (b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
            text = b[11]
            try:
                lang = single_detection(text, api_key=detect_languages_api)
                try:
                    translated_text = GoogleTranslator(source='auto', target='en').translate(text)
                    cv2.putText(img, translated_text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (50, 50, 255), 1)