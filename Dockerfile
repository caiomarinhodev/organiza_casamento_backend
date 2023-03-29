FROM python:3.8-bullseye

ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install -r requirements.txt

RUN ls

EXPOSE 8000