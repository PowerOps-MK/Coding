# pull official base image
FROM node:10

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

RUN npm create react-app example-react-app

# Installs all node packages
RUN npm install 

# Copies everything over to Docker environment
COPY . ./

CMD npm start
