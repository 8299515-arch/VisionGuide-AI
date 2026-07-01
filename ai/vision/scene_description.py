"""
VisionGuide AI - Scene Description Module (Sprint 2)
LLM-based scene understanding layer (stub + future vision model integration)
"""

from typing import Any, Dict, List


class SceneDescriber:
    """
    Combines object detection + OCR into semantic scene understanding
    """

    def __init__(self):
        pass

    def describe(self, objects: List[Dict[str, Any]], text: str) -> str:
        """
        Create human-readable scene description from CV outputs
        Sprint 2: rule-based + LLM-ready structure
        """

        if not objects and not text:
            return "No clear objects or text detected in the scene."

        parts = []

        if objects:
            parts.append(f"Detected {len(objects)} objects in the scene.")

        if text:
            parts.append(f"Visible text: {text}")

        return " ".join(parts)
