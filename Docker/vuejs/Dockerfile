# pull official base image node:19-alpine
FROM node@sha256:d5222e1ebd7dd7e9683f47a8861a4711cb4407a4830cbe04a582ca4986245700

# set working directory
WORKDIR /app

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

RUN npm install -g @vue/cli

RUN vue create example-vuejs-app --default --registry "https://registry.npmmirror.com"

WORKDIR /app/example-vuejs-app

# Start the service
CMD ["npm", "run", "serve"]
