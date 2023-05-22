# Specify the base image Node:19
FROM node@sha256:68ba78ba4a648b0eb50aa35b58126c88f6caa0ccbb5560b7487a7d4fb4b8e9e9

# Create a working directory inside the image
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# Create example application
RUN npm create react-app example-react-app

# Create a working directory inside the image
WORKDIR /app/example-react-app

# Download modules and dependencies
RUN npm install

# command to be used to execute when the image is used to start a container
CMD ["npm", "start"]
