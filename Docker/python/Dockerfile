# Specify the base image python:3.11-slim
FROM python@sha256:a5b723f5b78cb73300b647ff49fba4ceea22c5ec68c547fa3291978e6b692259

# Setup nonroot user
RUN adduser nonroot

# Use created user
USER nonroot

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files
COPY . .

# Download modules and dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to be used to execute when the image is used to start a container
CMD ["echo", "Hello"]
