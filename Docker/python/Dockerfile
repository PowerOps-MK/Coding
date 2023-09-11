# Specify the base image python:3.11-slim
FROM python@sha256:8488a4b1a393b0b2cb479a2da0a0d11cf816a77c0f9278205015148adadf9edf

# Setup nonroot user
RUN adduser nonroot
USER nonroot

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files
COPY . .

# Download modules and dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to be used to execute when the image is used to start a container
CMD ["echo", "Hello"]
