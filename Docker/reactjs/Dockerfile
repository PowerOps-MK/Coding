# Specify the base image Node:19
FROM node@sha256:57391181388cd89ede79f371e09373824051eb0f708165dcd0965f18b3682f35

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
