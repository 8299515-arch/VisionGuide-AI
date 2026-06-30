from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "VisionGuide AI"
    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str = "postgresql+asyncpg://vision:vision@db:5432/visionguide"
    REDIS_URL: str = "redis://redis:6379/0"

    JWT_SECRET: str = "CHANGE_ME_SUPER_SECRET"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    OPENAI_API_KEY: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
