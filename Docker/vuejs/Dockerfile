# Specify the base image node:19-alpine
FROM node@sha256:d5222e1ebd7dd7e9683f47a8861a4711cb4407a4830cbe04a582ca4986245700

# Download modules and dependencies
RUN npm install -g @vue/cli@5.0.8

# Create example application
RUN vue create example-vuejs-app --default --registry "https://registry.npmmirror.com"

# Create a working directory inside the image
WORKDIR /app/example-vuejs-app

# Copy directory files i.e all files 
COPY . .

RUN cat vue.config.js

# command to be used to execute when the image is used to start a container
CMD ["npm", "run", "serve"]
