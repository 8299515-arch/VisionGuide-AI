"""
VisionGuide AI - Global Error Handler (Sprint 3)
Standardized API error responses for production stability
"""

from fastapi import Request
from fastapi.responses import JSONResponse


class APIException(Exception):
    """Custom base exception for controlled API errors"""

    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


async def global_exception_handler(request: Request, exc: Exception):
    """Catch-all exception handler"""

    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": str(exc),
            "path": request.url.path
        }
    )


def api_exception_handler(request: Request, exc: APIException):
    """Handle known API exceptions"""

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "fail",
            "message": exc.message,
            "path": request.url.path
        }
    )
