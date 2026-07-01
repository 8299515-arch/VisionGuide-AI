"""
VisionGuide AI - v8.2 Vector Database Layer
- semantic memory foundation
- FAISS-style stub implementation
- ready for pgvector / FAISS upgrade
"""

from typing import List, Dict, Any
import math


class V8VectorDB:
    """
    Lightweight vector database simulation
    (production target: FAISS / pgvector)
    """

    def __init__(self):
        self.vectors: List[Dict[str, Any]] = []

    # ----------------------------
    # Storage
    # ----------------------------

    def add(self, embedding: List[float], payload: Dict[str, Any]):
        self.vectors.append({
            "embedding": embedding,
            "payload": payload
        })

    # ----------------------------
    # Similarity (cosine stub)
    # ----------------------------

    def _cosine(self, a: List[float], b: List[float]) -> float:
        dot = sum(x * y for x, y in zip(a, b))
        mag_a = math.sqrt(sum(x * x for x in a))
        mag_b = math.sqrt(sum(y * y for y in b))

        if mag_a == 0 or mag_b == 0:
            return 0.0

        return dot / (mag_a * mag_b)

    # ----------------------------
    # Search
    # ----------------------------

    def search(self, query_embedding: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        scored = []

        for item in self.vectors:
            score = self._cosine(query_embedding, item["embedding"])
            scored.append({
                "score": score,
                "payload": item["payload"]
            })

        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]


# singleton
vector_db = V8VectorDB()
