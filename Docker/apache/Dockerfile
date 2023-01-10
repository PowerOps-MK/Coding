# Specify the base image httpd:2.4.54
FROM httpd:2.4.54

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files
COPY ./src/html/ /usr/local/apache2/htdocs/
COPY . . 
