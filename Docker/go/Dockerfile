# specify the base image golang:1.19-alpine
FROM alpine@sha256:a9b24b67dc83b3383d22a14941c2b2b2ca6a103d805cac6820fd1355943beaf1

# create a working directory inside the image
WORKDIR /app

# copy directory files i.e all files ending with .go
COPY go.mod .

# download Go modules and dependencies
RUN go mod download

# compile application
RUN go build -v -o server

# command to be used to execute when the image is used to start a container
CMD ["/app/server"]
