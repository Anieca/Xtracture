import pyocr
from PIL import Image
from pyocr.builders import TextBuilder
from pathlib import Path
from google.cloud import vision


class LambdaRecognizer:
    def recognize(self, file_path: Path, lang: str = "") -> list[str]:
        return file_path.read_text().split("\n")


class GoogleVisionRecognizer:
    def __init__(self):
        self.client = vision.ImageAnnotatorClient()

    def recognize(self, file_path: Path, lang: str = "") -> list[str]:
        image = vision.Image(content=file_path.read_bytes())
        response = self.client.document_text_detection(image=image)
        return response.full_text_annotation.text.split("\n")


class TesseractRecognizer:
    def __init__(self) -> None:
        tools = pyocr.get_available_tools()
        assert len(tools) > 0

        self.tool = tools[0]
        assert hasattr(self.tool, "image_to_string")

        self.builder = TextBuilder(tesseract_layout=6)

    def recognize(self, file_path: Path, lang: str = "Japanese") -> list[str]:
        image = Image.open(file_path)
        text: str = self.tool.image_to_string(image, lang=lang, builder=self.builder)
        return text.split("\n")
