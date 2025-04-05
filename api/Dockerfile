FROM befair/uwsgi-python:latest

MAINTAINER Luca Ferroni "luca@befair.it"

ENV UWSGI_CHDIR     /code/api
ENV UWSGI_WSGI_FILE /code/api/run.py

COPY . /code/api

RUN pip install -r /code/api/deps/dev.txt

WORKDIR /code/api
