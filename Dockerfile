FROM python:3.7.2-slim

RUN apt update
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r /app/requirements.txt

COPY . /app

ENTRYPOINT sh ./docker-entry.sh
