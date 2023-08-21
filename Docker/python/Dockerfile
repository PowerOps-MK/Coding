# Specify the base image python:3.11-slim
FROM python@sha256:85b3d192dddbc96588b719e86991e472b390805a754681a38132de1977d8e429

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
