FROM python:3.8.0-slim

WORKDIR /app

COPY ./Python/spotify .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["echo", "Hello"]
