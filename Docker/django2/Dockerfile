# v3.7.3-slim
FROM python@sha256:250990a809a15bb6a3e307fec72dead200c882c940523fb1694baa78eb0e47c6 

# setup environment variable  
ENV DockerHOME=/data/Django2
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

COPY ./requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt
 
RUN django-admin startproject web .

COPY ./src .

EXPOSE $PORT

CMD ["python3.7", "manage.py", "runserver"]
