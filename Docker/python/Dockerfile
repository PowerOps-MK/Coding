# Specify the base image python:3.11-slim
FROM python@sha256:b7a504dd0affeb20cf1ba1d3219f854c889c7ad557a2a5a4c4aba19cadd075f1

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
