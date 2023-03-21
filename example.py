from pathlib import Path

from xtracture.extractor import GPTTextExtractor, TwoStageImageExtractor
from xtracture.recognizer import GoogleVisionRecognizer
from xtracture.schema import ExtractTarget


def main():
    image_recognizer = GoogleVisionRecognizer()
    text_extractor = GPTTextExtractor()
    image_extractor = TwoStageImageExtractor(image_recognizer, text_extractor)

    file_path = Path("./image.jpg")
    results = image_extractor.extract(
        file_path,
        [
            ExtractTarget(key="会社名", description="落札した会社の名前"),
            ExtractTarget(key="代表者名", description="落札した代表者の名前"),
        ],
    )
    print(results)


if __name__ == "__main__":
    main()
