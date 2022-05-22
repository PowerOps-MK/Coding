FROM python:3.7.3-slim

# setup environment variable  
ENV DockerHOME=/home/app/Django2
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

#COPY ./Python/django2 .

#RUN pip3 install -r requirements.txt

RUN pip install django djangorestframework
 
RUN django-admin startproject web .
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
