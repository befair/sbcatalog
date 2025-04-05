FROM python:3.13

MAINTAINER Luca Ferroni "luca@befair.it"

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code:/usr/local/lib/python3.13/site-packages

COPY . /code/test
RUN pip install -r /code/test/deps/dev.txt

WORKDIR /code
CMD ["true"]
