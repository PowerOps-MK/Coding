# pull official base image node:19-alpine
FROM node:19-alpine

# set working directory
WORKDIR /app

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# Installs all node packages
RUN npm install

RUN vue create example-vuejs-app --default

WORKDIR /app/example-vuejs-app

# Start the service
CMD ["npm", "run", "serve"]
