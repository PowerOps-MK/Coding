# Specify the base image node:19-alpine
FROM node@sha256:d5222e1ebd7dd7e9683f47a8861a4711cb4407a4830cbe04a582ca4986245700

# Create a working directory inside the image
WORKDIR /app

# Download modules and dependencies
RUN npm install -g @angular/cli@15.0.5

# Create example application
RUN ng new example-angular-app --defaults --skip-git

# Create a working directory inside the image
WORKDIR /app/example-angular-app

# Copy directory files i.e all files 
COPY . .

# command to be used to execute when the image is used to start a container
# CMD ["ng", "serve"]
ENV NODE_OPTIONS="--max-old-space-size=256"
CMD ["ng", "serve"]
