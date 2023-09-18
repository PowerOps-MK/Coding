# Specify the base image python:3.11-slim
FROM python@sha256:cc7372fe4746ca323f18c6bd0d45dadf22d192756abc5f73e39f9c7f10cba5aa

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
