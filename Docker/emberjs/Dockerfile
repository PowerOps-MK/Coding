# Specify the base image node:19-alpine
FROM node@sha256:d5222e1ebd7dd7e9683f47a8861a4711cb4407a4830cbe04a582ca4986245700

# Create a working directory inside the image
WORKDIR /app

# Download modules and dependencies
RUN npm install -g ember-cli@4.9.2

# Create example application
RUN ember new example-emberjs-app

# Create a working directory inside the image
WORKDIR /app/example-emberjs-app

# Copy directory files i.e all files 
# COPY . .

RUN ls

# command to be used to execute when the image is used to start a container
CMD ["npm", "start"]
