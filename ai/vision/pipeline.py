"""
VisionGuide AI - Vision Pipeline (Sprint 2)
Orchestrates object detection, OCR, and scene description modules.
"""

from typing import Dict, Any

from ai.vision.object_detection import ObjectDetector
from ai.vision.ocr import OCRReader
from ai.vision.scene_description import SceneDescriber


_detector = ObjectDetector()
_ocr = OCRReader()
_describer = SceneDescriber()


def process_image(image: str) -> Dict[str, Any]:
    """
    Main AI pipeline entry point (Sprint 2 real integration)
    """

    # 1. Object detection
    objects = _detector.detect(image)

    # 2. OCR
    ocr_result = _ocr.extract_text(image)
    text = ocr_result.get("text", "")

    # 3. Scene description
    description = _describer.describe(objects, text)

    return {
        "objects": objects,
        "text": text,
        "description": description
    }
