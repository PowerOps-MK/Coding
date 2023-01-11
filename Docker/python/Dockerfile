#Specify the base image python:3.11-slim
FROM python@sha256:1274a1fb3354baf78e80cc7485771175b506a4712e49e272765dceeb0528fad1

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files
COPY . .

# Download modules and dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to be used to execute when the image is used to start a container
CMD ["echo", "Hello"]
