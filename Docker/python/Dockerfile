FROM python:3.8-slim-buster

WORKDIR /app

COPY ./Docker/python/spotify .

RUN pip3 install -r requirements.txt

CMD ["echo", "Hello"]
