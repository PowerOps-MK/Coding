# Specify the base image python:3.11-slim
FROM python@sha256:f7382f4f9dbc51183c72d621b9c196c1565f713a1fe40c119d215c961fa22815

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
