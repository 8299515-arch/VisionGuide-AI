"""
VisionGuide AI - Object Detection Module (Sprint 2)
YOLOv8-based detection layer (initial stub + integration ready)
"""

from typing import List, Dict, Any


class ObjectDetector:
    """
    Wrapper around YOLOv8 model (Ultralytics)
    For Sprint 2 we keep it lightweight + mock-safe
    """

    def __init__(self, model_path: str = "yolov8n.pt"):
        self.model_path = model_path
        self.model = None

    def load_model(self):
        try:
            from ultralytics import YOLO
            self.model = YOLO(self.model_path)
        except Exception:
            self.model = None

    def detect(self, image) -> List[Dict[str, Any]]:
        if self.model is None:
            self.load_model()

        if self.model is None:
            return []

        try:
            results = self.model(image)
            detections = []

            for r in results:
                for box in r.boxes:
                    detections.append({
                        "class": int(box.cls[0]),
                        "confidence": float(box.conf[0]),
                        "bbox": box.xyxy[0].tolist()
                    })

            return detections

        except Exception:
            return []
