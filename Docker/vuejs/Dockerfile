# pull official base image node:19-alpine
FROM node:19-alpine

# install simple http server for serving static content
RUN npm install -g http-server

# set working directory
WORKDIR /app

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

# Start the service
CMD ["npm", "start"]
