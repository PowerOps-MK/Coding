# Specify the base image python:3.11-slim
FROM python@sha256:30f9c5b85d6a9866dd6307d24f4688174f7237bc3293b9293d590b1e59c68fc7

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
