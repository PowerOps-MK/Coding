# Specify the base image Node:19
FROM node@sha256:525d7cc45c28d0cc6ab50fe0abb6dd7620ed95489970fe5582cb77e8da2517a3

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
