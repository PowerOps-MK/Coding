FROM python:3.8-slim-buster

WORKDIR /app

COPY ./Python/spotify/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./Python .
