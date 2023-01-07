# Specify the base image python:3.7.3-slim
FROM python@sha256:250990a809a15bb6a3e307fec72dead200c882c940523fb1694baa78eb0e47c6

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files
COPY . . 

# Download modules and dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

RUN ls

# Command to be used to execute when the image is used to start a container
CMD ["python3.7", "app.py"]
