from pathlib import Path

from xtracture.extractor import Extractor
from xtracture.item_extractor import GPTItemExtractor
from xtracture.schema import ExtractTarget
from xtracture.text_extractor import GoogleVisionTextExtractor


def main():
    text_extractor = GoogleVisionTextExtractor()
    item_extractor = GPTItemExtractor()
    extractor = Extractor(text_extractor, item_extractor)

    file_path = Path("./image.jpg")
    results = extractor.extract(
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
