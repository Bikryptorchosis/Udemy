import cv2
import numpy as np
import pytesseract
import glob
import tqdm

try:
    from PIL import Image
except ImportError:
    import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def remove_noise(image):
    return cv2.medianBlur(image, 5)


def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


kupons = [f for f in glob.glob("*.jpg")]
print(kupons)

for kupon in tqdm.tqdm(kupons):
    print(kupon)
    img = cv2.imread('{}'.format(kupon))
    img = get_grayscale(img)
    img = thresholding(img)
    img = remove_noise(img)
    print(ocr_core(img))
    with open("kody.txt", "a") as file_object:
        file_object.write(ocr_core(img))
