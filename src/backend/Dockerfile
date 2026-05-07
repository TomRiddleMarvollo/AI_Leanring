FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for building certain packages if needed
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

COPY . .

# Expose port
EXPOSE 8000

# Start server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
