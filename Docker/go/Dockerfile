# Specify the base image golang:1.19-alpine
FROM golang@sha256:cfc9d1b07b1ef4f7a4571f0b60a99646a92ef76adb7d9943f4cb7b606c6554e2

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
