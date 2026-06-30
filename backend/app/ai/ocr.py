from pydantic import BaseModel
from typing import List
from PIL import Image
import io

# OCR AI module (MVP stub)
# Future upgrades:
# - PaddleOCR / Tesseract / EasyOCR
# - multilingual recognition
# - packaging & medicine label understanding
# - real-time camera OCR stream


class OCRResponse(BaseModel):
    text: str
    language: str
    confidence: float


async def extract_text(image_bytes: bytes) -> OCRResponse:
    """
    MVP OCR processor (stub implementation)
    """

    try:
        image = Image.open(io.BytesIO(image_bytes))
        width, height = image.size

        # MOCK OCR OUTPUT
        text = f"Detected text from image {width}x{height}: 'Sample label text'"

        return OCRResponse(
            text=text,
            language="en",
            confidence=0.75,
        )

    except Exception as e:
        return OCRResponse(
            text=f"OCR error: {str(e)}",
            language="unknown",
            confidence=0.0,
        )