FROM python:3.8.0-slim

WORKDIR /app

COPY ./Docker/spotify/requirements.txt ./

RUN pip install -r requirements.txt

COPY ./Docker/spotify .

CMD ["echo", "Hello"]
