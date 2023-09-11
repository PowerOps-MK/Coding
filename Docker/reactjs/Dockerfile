# Specify the base image Node:19
FROM node@sha256:69cf8e7dcc78e63db74ca6ed570e571e41029accdac21b219b6ac57e9aca63cf

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
