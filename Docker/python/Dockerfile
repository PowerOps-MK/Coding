# Specify the base image python:3.11-slim
FROM python@sha256:2dd2f9000021839e8fba0debd8a2308c7e26f95fdfbc0c728eeb0b5b9a8c6a39

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
