FROM python:3.11-slim

WORKDIR /app

COPY libraries.txt .
RUN pip install --no-cache-dir -r libraries.txt

COPY . .

CMD ["python3"]