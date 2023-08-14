# Specify the base image golang:1.19-alpine
FROM golang@sha256:ec457a2fcd235259273428a24e09900c496d0c52207266f96a330062a01e3622

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
