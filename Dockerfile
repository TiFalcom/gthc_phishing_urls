# syntax=docker/dockerfile:1

FROM python:3.9-slim

#WORKDIR /app


COPY app /app/
COPY models /models/
COPY src /src/
COPY requirements.txt requirements.txt

RUN echo ls
RUN pip install -r requirements.txt

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]