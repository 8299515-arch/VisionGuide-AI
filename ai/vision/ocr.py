"""
VisionGuide AI - OCR Module (Sprint 2)
EasyOCR-based text extraction layer (safe stub + integration ready)
"""

from typing import Any, Dict


class OCRReader:
    """
    OCR engine wrapper using EasyOCR
    Sprint 2: lazy-loaded + fallback-safe
    """

    def __init__(self, languages=None):
        self.languages = languages or ['en']
        self.reader = None

    def load(self):
        try:
            import easyocr
            self.reader = easyocr.Reader(self.languages)
        except Exception:
            self.reader = None

    def extract_text(self, image: Any) -> Dict[str, Any]:
        if self.reader is None:
            self.load()

        if self.reader is None:
            return {"text": ""}

        try:
            result = self.reader.readtext(image)
            text = " ".join([r[1] for r in result])
            return {"text": text}
        except Exception:
            return {"text": ""}
