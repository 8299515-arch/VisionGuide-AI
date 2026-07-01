"""
VisionGuide AI - Metrics (Sprint 3)
Simple in-memory metrics for observability
"""

from collections import defaultdict


class MetricsStore:
    def __init__(self):
        self.request_count = 0
        self.error_count = 0
        self.total_latency = 0.0
        self.endpoint_hits = defaultdict(int)

    def record_request(self, path: str, latency: float):
        self.request_count += 1
        self.total_latency += latency
        self.endpoint_hits[path] += 1

    def record_error(self):
        self.error_count += 1

    def avg_latency(self):
        if self.request_count == 0:
            return 0.0
        return self.total_latency / self.request_count


metrics = MetricsStore()