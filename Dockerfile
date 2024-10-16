FROM python:3.9-slim

RUN apt-get update && apt-get install -y git && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

# RUN git clone --branch dev https://github.com/josearcos2023/thesisBackCanvasApi.git .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app 

COPY .env /app/.env

EXPOSE 5000

CMD ["python", "app.py"]