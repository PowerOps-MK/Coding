# 
FROM mcr.microsoft.com/windows/servercore/iis

# Create a working directory inside the image
WORKDIR /inetpub/wwwroot

# Remove old files
RUN powershell -NoProfile -Command Remove-Item -Recurse C:\inetpub\wwwroot\*

# Copy directory files i.e all files 
COPY . .

# command to be used to execute when the image is used to start a container








