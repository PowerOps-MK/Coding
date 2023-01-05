# pull official base image
FROM node@sha256:d5222e1ebd7dd7e9683f47a8861a4711cb4407a4830cbe04a582ca4986245700 #v19

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

RUN npm create react-app example-react-app

WORKDIR /app/example-react-app

# Installs all node packages
RUN npm install

# Start the service
CMD ["npm", "start"]
