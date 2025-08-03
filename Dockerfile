FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
COPY main.py .

CMD ["bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 8088 --reload"]

EXPOSE 8088