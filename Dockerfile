FROM python:3.8

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

USER root