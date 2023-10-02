# Specify the base image Node:19
FROM node@sha256:6b3f9aa7eefa8d4c93d43914e78aa2bfea9a12808b0059e5da78854dfa8b8768

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
