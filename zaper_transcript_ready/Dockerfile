FROM python:3.12-slim

WORKDIR /app

# 1) dependências de sistema
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# 2) dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3) código
COPY app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
