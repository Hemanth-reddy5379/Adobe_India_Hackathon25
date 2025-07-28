FROM python:3.10-slim

WORKDIR /app

# ✅ Install only system dependencies once
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libglib2.0-0 libgl1-mesa-glx \
 && rm -rf /var/lib/apt/lists/*

# ✅ Copy only requirements first, so this step is cached
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ✅ Then copy the rest of the app
COPY . .

CMD ["python", "main.py"]
