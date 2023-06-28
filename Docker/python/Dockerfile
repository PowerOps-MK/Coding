# Specify the base image python:3.11-slim
FROM python@sha256:fe68f3194a1a6df058901085495abca83d8841415101366c3a4c66f06f39760a

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
