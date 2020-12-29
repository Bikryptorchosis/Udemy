import cv2
import pytesseract
import glob
try:
    from PIL import Image
except ImportError:
    import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


kupons = [f for f in glob.glob("*.jpg")]
print(kupons)

for kupon in kupons:
    print(kupon)
    img = cv2.imread("{}".format(kupon))
    # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_rgb = Image.frombytes('RGB', img.shape[:2], img, 'raw', 'BGR', 0, 0)
    text = pytesseract.image_to_string(img_rgb)
    print(text)
    # text = pytesseract.image_to_string(img, config='--psm 7 -c tessedit_char_whitelist=abcdefghijkLmnoprstuwxyzq0123456789')
    # print(pytesseract.image_to_string(Image.open(img_rgb)))

