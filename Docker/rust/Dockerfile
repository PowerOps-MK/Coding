#Specify the base image rust:1.66-slim
FROM rust:1.66-slim

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files
COPY . .

# Download modules and dependencies
RUN cargo install --path .

# Command to be used to execute when the image is used to start a container
CMD ["echo", "Hello"]
