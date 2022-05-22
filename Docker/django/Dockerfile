FROM python:3.8.0-slim

# setup environment variable  
ENV DockerHOME=/home/app/Django2

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

COPY ./Docker/django .

RUN pip3 install -r requirements.txt

EXPOSE 8000

# start server  
CMD python3.8 manage.py runserver  
