# Xtracture: Open Source Document Content Extractuion Library

Xtracture is an open source library designed to efficiently extract arbitrary elements from documents.

## Features

- Natural language rule creation using LLMs
- Switchable OCR engines for optimized perfomance and accuracy

## prerequirements

- OpenAI API Key (for LLM rule creation)

## Installation

```
pip install -U xtracture
```

## Usage

### Use Google Cloud Vision API

Google CLoud Vision Credentials must be correctly configured.

see `examples/google_cloud_vision_example.py`.

### Use Tesseract

Tesseract must be installed beforehand.

see `examples/tesseract_example.py`.

### Use only GPT Extractor

You can input OCR-processed text file.
see `examples/lambda_example.py`.

## License

Xtracture is released under the MIT License.
