# golang:1.16-alpine
FROM golang@sha256:660f138b4477001d65324a51fa158c1b868651b44e43f0953bf062e9f38b72f3

WORKDIR /app

COPY go.mod ./
COPY go.sum ./
RUN go mod download

COPY *.go ./

RUN go build -o /docker-gs-ping

# EXPOSE 8080

CMD [ "/docker-gs-ping" ]
