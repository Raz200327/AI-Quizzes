import pytesseract
from PIL import Image
import os

class LectureSlides:
    def __init__(self, slide_directory):
        pytesseract.pytesseract.tesseract_cmd = r"./tesseract"
        self.slide_directory = slide_directory

    def image_extract(self):
        self.text = pytesseract.image_to_string(Image.open(f"./media/{self.slide_directory}")).replace("\n", " ")
        return self.text

