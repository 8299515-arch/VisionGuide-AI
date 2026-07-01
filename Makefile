# VisionGuide AI - One click runner

.PHONY: run dev docker-up docker-build test

# Run backend locally
run:
	uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000

# Dev alias
dev:
	uvicorn backend.app.main:app --reload

# Run with Docker Compose
docker-up:
	docker-compose up --build

# Build Docker image
docker-build:
	docker build -t visionguide-ai .

# Run tests
test:
	pytest -q
