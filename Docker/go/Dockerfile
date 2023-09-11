# Specify the base image golang:1.19-alpine
FROM golang@sha256:d2aad22fc6f1017aa568d980b15d0067a721c770be47b9dc62b11c33487fba64

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files 
COPY . .

# Download modules and dependencies
RUN go mod download

# Compile application
RUN go build -v -o server

# command to be used to execute when the image is used to start a container
CMD ["/app/server"]
