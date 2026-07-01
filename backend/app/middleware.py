"""
VisionGuide AI - Middleware (Sprint 3)
Logging + error handling layer for production stability
"""

import time
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


logger = logging.getLogger("visionguide")
logger.setLevel(logging.INFO)


class LoggingMiddleware(BaseHTTPMiddleware):
    """Logs request/response timing and status"""

    async def dispatch(self, request: Request, call_next):
        start = time.time()

        try:
            response = await call_next(request)
            duration = time.time() - start

            logger.info(
                f"{request.method} {request.url.path} -> {response.status_code} in {duration:.3f}s"
            )

            return response

        except Exception as e:
            duration = time.time() - start

            logger.error(
                f"ERROR {request.method} {request.url.path} after {duration:.3f}s: {str(e)}"
            )

            raise
