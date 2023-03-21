from pathlib import Path
from typing import Protocol

from pydantic import BaseModel


class ExtractTarget(BaseModel):
    key: str
    description: str


class ExtractedResult(BaseModel):
    key: str
    values: list[str]


class IRecognizer(Protocol):
    def recognize(self, file_path: Path) -> list[str]:
        ...


class IExtractor(Protocol):
    def extract(self, texts: list[str], targets: list[ExtractTarget]) -> list[ExtractedResult]:
        ...
