from pathlib import Path
from typing import Any

import pyocr
from google.cloud import vision
from PIL import Image
from pyocr.builders import TextBuilder


class LambdaTextExtractor:
    @staticmethod
    def extract(file_path: Path, lang: str = "") -> list[str]:
        return file_path.read_text().split("\n")


class GoogleVisionTextExtractor:
    def __init__(self):
        self.client = vision.ImageAnnotatorClient()

    def extract(self, file_path: Path, lang: str = "") -> list[str]:
        image = vision.Image(content=file_path.read_bytes())
        response = self.client.document_text_detection(image=image)
        return response.full_text_annotation.text.split("\n")


class TesseractTextExtractor:
    def __init__(self) -> None:
        tools: list[Any] = pyocr.get_available_tools()
        if len(tools) == 0:
            raise RuntimeError("Tesseract does not configured correctly.")

        self.tool = tools[0]
        assert hasattr(self.tool, "image_to_string")

        self.builder = TextBuilder(tesseract_layout=6)

    def extract(self, file_path: Path, lang: str = "Japanese") -> list[str]:
        image = Image.open(file_path)
        text: str = self.tool.image_to_string(image, lang=lang, builder=self.builder)
        return text.split("\n")
