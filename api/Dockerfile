FROM kobe25/uwsgi-python:latest

MAINTAINER Antonio Esposito "kobe@befair.it"

ENV UWSGI_CHDIR     /code/api
ENV UWSGI_WSGI_FILE /code/api/run.py

COPY . /code/api

RUN pip install -r /code/api/deps/dev.txt

WORKDIR /code/api
