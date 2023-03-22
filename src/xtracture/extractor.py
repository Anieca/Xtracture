from pathlib import Path

from .schema import ExtractTarget, IItemExtractor, Item, ITextExtractor


class Extractor:
    def __init__(self, text_extractor: ITextExtractor, item_extractor: IItemExtractor) -> None:
        self.text_extractor = text_extractor
        self.item_extractor = item_extractor

    def extract(self, file_path: Path, targets: list[ExtractTarget]) -> list[Item]:
        texts = self.text_extractor.extract(file_path)
        return self.item_extractor.extract_from_text(texts, targets)
