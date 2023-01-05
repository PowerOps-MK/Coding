# v3.8.0-slim
FROM python@sha256:250990a809a15bb6a3e307fec72dead200c882c940523fb1694baa78eb0e47c6

WORKDIR /app

COPY ./Python/spotify .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["echo", "Hello"]
