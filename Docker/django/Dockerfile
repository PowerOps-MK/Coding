FROM python:3.7.3-slim

# setup environment variable  
ENV DockerHOME=/home/app/Django2
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

COPY ./Python/django2 .

RUN pip3 install -r requirements.txt

EXPOSE 8000

# start server  
CMD python3.8 manage.py runserver  
