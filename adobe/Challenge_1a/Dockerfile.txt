FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    poppler-utils \
    tesseract-ocr \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY process_pdfs.py utils.py ./

CMD ["python", "process_pdfs.py"]
