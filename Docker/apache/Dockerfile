# Specify the base image httpd:2.4.54
FROM httpd@sha256:f8c7bdfa89fb4448c95856c6145359f67dd447134018247609e7a23e5c5ec03a

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files
COPY ./src/html/ /usr/local/apache2/htdocs/
COPY . . 

RUN ls /etc/apache2/
