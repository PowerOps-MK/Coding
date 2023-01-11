# Specify the base image python:3.11-slim
FROM python@sha256:ad1b4d1fd5c1efee69c2da4659b0762fc068e8edff972b39d68fd631db9bb20a

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files
COPY . . 

# Download modules and dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Command to be used to execute when the image is used to start a container
CMD ["python3", "app.py"]
