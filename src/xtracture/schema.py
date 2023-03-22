from pathlib import Path
from typing import Protocol

from pydantic import BaseModel


class ExtractTarget(BaseModel):
    key: str
    description: str = ""
    constraint: str = ""


class Item(BaseModel):
    key: str
    values: list[str]


class ITextExtractor(Protocol):
    def extract(self, file_path: Path, lang: str = "") -> list[str]:
        ...


class IItemExtractor(Protocol):
    def extract_from_text(self, texts: list[str], targets: list[ExtractTarget]) -> list[Item]:
        ...
