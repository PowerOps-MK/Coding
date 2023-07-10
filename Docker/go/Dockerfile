# Specify the base image golang:1.19-alpine
FROM golang@sha256:fd9306e1c664bd49a11d4a4a04e41303430e069e437d137876e9290a555e06fb

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
