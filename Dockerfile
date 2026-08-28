# ==============================================================================
# ElewaSTEM (Mwalimu STEM) — Google Cloud Run Production Dockerfile
# Optimized for Google Cloud Run, Cloud Build, and Vertex AI / Gemini API
# ==============================================================================

FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080 \
    HOST=0.0.0.0

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency specifications
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application backend and frontend
COPY backend/ /app/backend/
COPY frontend/ /app/frontend/
COPY run.py /app/run.py

# Expose port (Default Cloud Run port is 8080)
EXPOSE 8080

# Healthcheck for Google Cloud Run
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/api/health || exit 1

# Run FastAPI via Uvicorn on Cloud Run
CMD ["python", "-m", "uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8080"]
