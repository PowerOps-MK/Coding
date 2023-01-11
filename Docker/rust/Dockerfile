#Specify the base image rust:1.66-slim
FROM rust@sha256:5a051df475304059c221f6a6b8ba41b49cf1d703b72765dafec3db98c241e2cc

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files
COPY . .

# Download modules and dependencies
RUN cargo install --path .

# Command to be used to execute when the image is used to start a container
CMD ["echo", "Hello"]
