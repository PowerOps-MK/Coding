#Specify the base image alpine:3.17.1
FROM alpine:3.17.1

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files
COPY . .

# Download modules and dependencies
# RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
