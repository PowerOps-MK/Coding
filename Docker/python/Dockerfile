# Specify the base image python:3.11-slim
FROM python@sha256:b9683fa80e22970150741c974f45bf1d25856bd76443ea561df4e6fc00c2bc17

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
