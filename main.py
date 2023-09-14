import cv2
import pytesseract
from PIL import Image

TESSERACT_PATH = r'/opt/homebrew/Cellar/tesseract/5.3.2_1/bin/tesseract'

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def extract_headlines(image_path):
    image = cv2.imread(image_path)
    gray_image = get_grayscale(image)
    threshold_img = thresholding(gray_image)
    text = pytesseract.image_to_string(threshold_img)
    lines = text.strip().split("\n")
    headlines = [line for line in lines if line.isupper()]
    return headlines

if __name__ == '__main__':
    image_path = '1.png' # locally downloaded file renamed - TODO tweak for CI/CD
    headlines = extract_headlines(image_path)
    
    if headlines:
        for idx, headline in enumerate(headlines, 1):
            print(f"{idx}. {headline}")
    else:
        print("No headlines found.")
