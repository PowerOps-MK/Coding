FROM python:3.7.3-slim

# setup environment variable  
ENV DockerHOME=/home/app/Django2
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

COPY . .

RUN pip3 install -r requirements.txt
 
RUN django-admin startproject web .

RUN echo "ALLOWED_HOSTS = ['*']" | tee -a /home/app/Django2/web/settings.py 

RUN python3.7 manage.py startapp polls

COPY . ./web

CMD python3.7 manage.py runserver 0.0.0.0:$PORT
