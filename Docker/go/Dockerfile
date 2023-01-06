# specify the base image golang:1.19-buster
FROM golang:1.19-buster

# create a working directory inside the image
WORKDIR /app

# copy directory files i.e all files ending with .go
COPY . .

# download Go modules and dependencies
RUN go mod download

# compile application
RUN go build -v -o server

# command to be used to execute when the image is used to start a container
CMD ["/app/server"]
