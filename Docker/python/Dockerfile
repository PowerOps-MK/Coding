# Specify the base image python:3.11-slim
FROM python@sha256:380d708853b1564b71ad3744a69895d552099f618df60741c5d4a9e9e65873b9

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
