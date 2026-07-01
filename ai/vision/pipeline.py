"""
VisionGuide AI - Vision Pipeline (Sprint 1)
Orchestrates object detection, OCR, and scene description modules.
"""

from typing import Dict, Any


def process_image(image: str) -> Dict[str, Any]:
    """
    Main AI pipeline entry point (mock version for Sprint 1)
    """

    objects = detect_objects(image)
    text = extract_text(image)
    description = describe_scene(image)

    return {
        "objects": objects,
        "text": text,
        "description": description
    }


def detect_objects(image: str):
    # TODO: integrate YOLO / DETR
    return []


def extract_text(image: str):
    # TODO: integrate OCR engine
    return ""


def describe_scene(image: str):
    # TODO: integrate LLM vision captioning
    return "VisionGuide AI: mock scene description"
