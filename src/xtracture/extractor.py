from typing import Any
from pathlib import Path

from langchain.llms import OpenAIChat
from langchain import PromptTemplate

from .logger import setup_logger
from .schema import IExtractor, IRecognizer, ExtractedResult, ExtractTarget

logger = setup_logger(__name__)


class GPTTextExtractor:
    TEMPLATE = """Carry out the following instructions.
* Correct any OCR errors in the input text
* Extract the following items according to the given constraints
|Item|Constraint|
{extract_targets}
* Review the extracted results and point out any errors
* If there are any errors, correct them and output the extraction results again
* Output the extraction results in JSON format, enclosed in triple backticks (set the key as string type and the value as array type)

The text is as follows.
{text}
"""

    def __init__(self, model_name: str = "gpt-3.5-turbo") -> None:
        self.gpt = OpenAIChat(model_name=model_name, temperature=1)  # type: ignore
        self.prompt = PromptTemplate(input_variables=["extract_targets", "text"], template=self.TEMPLATE)

    def extract(self, texts: list[str], targets: list[ExtractTarget]) -> list[ExtractedResult]:
        extract_targets = "\n".join([f"|{t.key}|{t.description}|" for t in targets])

        inputs = self.prompt.format(extract_targets=extract_targets, text="\n".join(texts))
        logger.info(inputs)
        outputs = self.gpt(inputs)
        logger.info(outputs)

        results: dict[str, Any]
        try:
            *_, json_output, _ = outputs.split("```")
            results = eval(json_output.replace("json", ""))
        except Exception:
            logger.exception(self.__class__.__name__)
            results = {}
        return [ExtractedResult(key=target.key, values=results.get(target.key, [])) for target in targets]


class TwoStageImageExtractor:
    def __init__(self, recognizer: IRecognizer, extractor: IExtractor) -> None:
        self.recognizer = recognizer
        self.text_extractor = extractor

    def extract(self, file_path: Path, targets: list[ExtractTarget]) -> list[ExtractedResult]:
        texts = self.recognizer.recognize(file_path)
        return self.text_extractor.extract(texts, targets)


class OneStageImageExtractor:
    def __init__(self, extractor: IExtractor) -> None:
        self.extractor = extractor
