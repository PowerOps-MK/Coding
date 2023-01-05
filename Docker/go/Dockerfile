# specify the base image golang:1.17-alpine
FROM golang:1.17-alpine

# create a working directory inside the image
WORKDIR /app

# copy directory files i.e all files ending with .go
COPY *.go ./

# download Go modules and dependencies
RUN go mod download

# compile application
RUN go build -o /godocker

# command to be used to execute when the image is used to start a container
CMD [ "/godocker" ]
