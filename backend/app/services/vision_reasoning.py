"""
VisionGuide AI - v2 Brain Layer
LLM-style reasoning + vision interpretation orchestrator
"""

from typing import Dict, Any

class VisionReasoningEngine:
    """
    v2 cognitive layer:
    - interprets vision pipeline output
    - generates structured reasoning
    - prepares human-friendly accessibility responses
    """

    def __init__(self):
        self.memory = []  # lightweight session memory (MVP)

    def remember(self, item: Dict[str, Any]):
        self.memory.append(item)
        if len(self.memory) > 50:
            self.memory.pop(0)

    def reason(self, vision_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Core reasoning pipeline
        """
        objects = vision_data.get("objects", [])
        text = vision_data.get("text", "")
        description = vision_data.get("description", "")

        # Simple structured reasoning (v2 baseline)
        navigation_hint = self._generate_navigation_hint(objects)
        accessibility_summary = self._generate_summary(objects, text, description)

        result = {
            "summary": accessibility_summary,
            "navigation_hint": navigation_hint,
            "confidence": self._estimate_confidence(vision_data)
        }

        self.remember(result)
        return result

    def _generate_summary(self, objects, text, description):
        parts = []

        if description:
            parts.append(f"Scene: {description}")

        if objects:
            parts.append(f"Detected objects: {', '.join(objects[:10])}")

        if text:
            parts.append(f"Visible text: {text[:200]}")

        return " | ".join(parts)

    def _generate_navigation_hint(self, objects):
        if not objects:
            return "Move slowly forward, no obstacles detected"

        if "person" in objects:
            return "Person detected nearby, adjust path carefully"

        if any(o in objects for o in ["car", "vehicle"]):
            return "Traffic object detected, stop or change direction"

        return "Proceed with caution, objects detected ahead"

    def _estimate_confidence(self, vision_data):
        score = 0.5

        if vision_data.get("objects"):
            score += 0.2
        if vision_data.get("text"):
            score += 0.2
        if vision_data.get("description"):
            score += 0.1

        return round(min(score, 0.99), 2)


# singleton
engine = VisionReasoningEngine()
