from typing import Optional

from app.ai.voice_alerts import VoiceAlertEngine, VoiceAlert

# AI Event Orchestrator (Core Brain Layer)
# Combines Vision, OCR, Navigation into a unified decision system
# Future upgrade: priority queue + context memory + LLM reasoning


class AIEventOrchestrator:
    """
    Central brain of VisionGuide AI.
    Decides what the user should hear NOW.
    """

    def __init__(self):
        self.alert_engine = VoiceAlertEngine()
        self.last_event: Optional[str] = None

    def process_vision(self, description: str, danger_level: str) -> Optional[VoiceAlert]:
        """
        Handle real-time vision AI output
        """
        self.last_event = "vision"
        return self.alert_engine.process_vision_event(description, danger_level)

    def process_navigation(self, instruction: str, is_turn: bool = False) -> VoiceAlert:
        """
        Handle navigation instructions
        """
        self.last_event = "navigation"
        return self.alert_engine.process_navigation_event(instruction, is_turn)

    def process_ocr(self, text: str) -> VoiceAlert:
        """
        Handle OCR text reading events
        """
        self.last_event = "ocr"
        return VoiceAlert(
            message=f"Text detected: {text}",
            level=self.alert_engine.process_vision_event("", "low").level
        )

    def decide_priority(self, events: list[str]) -> str:
        """
        Simple priority logic (MVP)
        Future: AI-based context ranking
        """
        if "danger" in events:
            return "vision"
        if "navigation" in events:
            return "navigation"
        if "ocr" in events:
            return "ocr"
        return "idle"
