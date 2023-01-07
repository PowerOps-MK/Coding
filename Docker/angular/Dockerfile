# Specify the base image node:19-alpine
FROM node@sha256:d5222e1ebd7dd7e9683f47a8861a4711cb4407a4830cbe04a582ca4986245700

ENV NODE_OPTIONS="--max_old_space_size=8048"

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

RUN node --max_old_space_size=8192

# command to be used to execute when the image is used to start a container
CMD ["ng", "serve"]
