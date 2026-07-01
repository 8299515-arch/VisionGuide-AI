"""
VisionGuide AI - TTS Module (Sprint 2)
Text-to-Speech layer for accessibility output
"""

from typing import Optional


class TTS:
    """
    Simple TTS wrapper (Sprint 2)
    Can use pyttsx3 or system voice in future
    """

    def __init__(self):
        self.engine = None

    def load(self):
        try:
            import pyttsx3
            self.engine = pyttsx3.init()
        except Exception:
            self.engine = None

    def speak(self, text: str, lang: Optional[str] = "en") -> bool:
        """
        Convert text to speech
        """

        if not text:
            return False

        if self.engine is None:
            self.load()

        if self.engine is None:
            return False

        try:
            self.engine.say(text)
            self.engine.runAndWait()
            return True
        except Exception:
            return False
