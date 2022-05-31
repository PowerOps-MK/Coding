# pull official base image
FROM node

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

RUN npm create react-app example-react-app

WORKDIR /app/example-react-app

# Installs all node packages
RUN npm install

EXPOSE $PORT

CMD npm start
