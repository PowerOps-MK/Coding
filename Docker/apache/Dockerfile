# Specify the base image httpd:2.4.54
FROM httpd:2.4.54

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files
COPY . . 

# Download modules and dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Command to be used to execute when the image is used to start a container
CMD ["python3", "app.py"]
