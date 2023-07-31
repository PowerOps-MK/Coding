# Specify the base image golang:1.19-alpine
FROM golang@sha256:010a0ffe47398a3646993df44906c065c526eabf309d01fb0cbc9a5696024a60

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
