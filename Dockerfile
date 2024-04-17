# syntax=docker/dockerfile:1

FROM python:3.12-slim

WORKDIR /app

#COPY requirements.txt requirements.txt

COPY app models src requeriments.txt ./

RUN pip install -r requirements.txt



CMD [ "uvicorn", "app.main:app"]