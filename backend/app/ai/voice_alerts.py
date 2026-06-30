from enum import Enum
from typing import Optional

# Voice Alert System (MVP)
# Converts AI events into prioritized spoken alerts


class AlertLevel(str, Enum):
    INFO = "info"
    WARNING = "warning"
    DANGER = "danger"


class VoiceAlert:
    def __init__(self, message: str, level: AlertLevel):
        self.message = message
        self.level = level


class VoiceAlertEngine:
    """
    Prioritizes and formats real-time AI events
    for voice output (TTS layer).
    """

    def __init__(self):
        self.last_alert: Optional[VoiceAlert] = None

    def process_vision_event(self, description: str, danger_level: str) -> Optional[VoiceAlert]:
        """
        Convert vision AI output into voice alert
        """

        if danger_level == "high":
            alert = VoiceAlert("Warning! Immediate obstacle ahead!", AlertLevel.DANGER)
        elif danger_level == "medium":
            alert = VoiceAlert("Caution, obstacle detected nearby.", AlertLevel.WARNING)
        else:
            alert = VoiceAlert(description, AlertLevel.INFO)

        self.last_alert = alert
        return alert

    def process_navigation_event(self, instruction: str, is_turn: bool = False) -> VoiceAlert:
        if is_turn:
            message = f"Turn instruction: {instruction}"
        else:
            message = instruction

        alert = VoiceAlert(message, AlertLevel.INFO)
        self.last_alert = alert
        return alert