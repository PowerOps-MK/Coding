# Specify the base image golang:1.19-alpine
FROM golang@sha256:19600fdcae402165dcdab18cb9649540bde6be7274dedb5d205b2f84029fe909

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
