FROM python:3.7.3-slim

# setup environment variable  
ENV DockerHOME=/data/Django2
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
 
RUN django-admin startproject web .

RUN python3.7 manage.py startapp polls

COPY ./src .

RUN python3.7 manage.py migrate

CMD python3.7 manage.py runserver 0.0.0.0:$PORT
