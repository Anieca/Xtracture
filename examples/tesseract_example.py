from pathlib import Path

from xtracture.extractor import GPTTextExtractor, TwoStageImageExtractor
from xtracture.recognizer import TesseractRecognizer
from xtracture.schema import ExtractTarget


def main():
    image_recognizer = TesseractRecognizer()

    text_extractor = GPTTextExtractor()
    image_extractor = TwoStageImageExtractor(image_recognizer, text_extractor)

    file_path = Path("./image.jpg")
    results = image_extractor.extract(
        file_path,
        [
            ExtractTarget(key="会社名", description="会社の名前"),
            ExtractTarget(key="代表者名", description="代表者の名前"),
            ExtractTarget(key="収入金額", description="収入の合計金額"),
        ],
    )
    print(results)


if __name__ == "__main__":
    main()
