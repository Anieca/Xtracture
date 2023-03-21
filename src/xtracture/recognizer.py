from pathlib import Path
from google.cloud import vision


class MockRecognizer:
    def recognize(self, file_path: Path) -> list[str]:
        return file_path.read_text().split("\n")


class GoogleVisionRecognizer:
    def __init__(self):
        self.client = vision.ImageAnnotatorClient()

    def recognize(self, file_path: Path) -> list[str]:
        image = vision.Image(content=file_path.read_bytes())
        response = self.client.document_text_detection(image=image)
        return response.full_text_annotation.text.split("\n")
