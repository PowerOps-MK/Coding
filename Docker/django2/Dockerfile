# Specify the base image python:3.7.3-slim
FROM python@sha256:cc7372fe4746ca323f18c6bd0d45dadf22d192756abc5f73e39f9c7f10cba5aa

# Setup environment variable  
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a working directory inside the image
WORKDIR /data/Django2

# Copy directory files i.e all files
COPY . . 

# Download modules and dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Compile application
RUN django-admin startproject web .

# Command to be used to execute when the image is used to start a container
CMD ["python3.7", "manage.py", "runserver"]
