FROM python:3.7.3-slim

# setup environment variable  
ENV DockerHOME=/data/Django2
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_PASSWORD=random09//5
ENV DJANGO_SUPERUSER_USERNAME=testuser
ENV DJANGO_SUPERUSER_EMAIL=testuser@mail.com

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
 
RUN django-admin startproject web .

RUN python3.7 manage.py startapp polls

COPY ./src .

RUN python3.7 manage.py makemigrations polls

RUN python3.7 manage.py migrate

RUN python3.7 manage.py createsuperuser --noinput

CMD python3.7 manage.py runserver 0.0.0.0:$PORT
