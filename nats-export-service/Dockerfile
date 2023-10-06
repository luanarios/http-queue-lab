# Use uma imagem base Python
FROM python:3.9-slim

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "/app/app.py"]