# Specify the base image powershell:alpine-3.15
FROM mcr.microsoft.com/powershell@sha256:f1811b16d5fc03d6e9081208211497e753e95ac74a3fafdf899e62c9c4929e01

# Create a working directory inside the image
WORKDIR /app

# Copy directory files i.e all files 
COPY . .

# Download modules and dependencies
RUN pwsh -h
