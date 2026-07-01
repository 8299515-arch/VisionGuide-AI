"""
VisionGuide AI - Vision Pipeline (Sprint 2)
Orchestrates object detection, OCR, scene description, and voice output modules.
"""

from typing import Dict, Any

from ai.vision.object_detection import ObjectDetector
from ai.vision.ocr import OCRReader
from ai.vision.scene_description import SceneDescriber
from ai.vision.tts import TTS


_detector = ObjectDetector()
_ocr = OCRReader()
_describer = SceneDescriber()
_tts = TTS()


def process_image(image: str, voice: bool = False) -> Dict[str, Any]:
    """
    Main AI pipeline entry point (Sprint 2 full integration)
    """

    # 1. Object detection
    objects = _detector.detect(image)

    # 2. OCR
    ocr_result = _ocr.extract_text(image)
    text = ocr_result.get("text", "")

    # 3. Scene description
    description = _describer.describe(objects, text)

    # 4. Voice output (optional)
    spoken = False
    if voice:
        spoken = _tts.speak(description)

    return {
        "objects": objects,
        "text": text,
        "description": description,
        "voice_output": spoken
    }
