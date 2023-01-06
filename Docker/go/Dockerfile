# Specify the base image golang:1.19-alpine
FROM golang@sha256:660f138b4477001d65324a51fa158c1b868651b44e43f0953bf062e9f38b72f3

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
