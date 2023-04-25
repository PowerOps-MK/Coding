# Specify the base image golang:1.19-alpine
FROM golang@sha256:403f48633fb5ebd49f9a2b6ad6719f912df23dae44974a0c9445be331e72ff5e

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
