FROM python:3.4

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code:/usr/local/lib/python3.4/site-packages

COPY . /code/test
RUN pip install -r /code/test/deps/dev.txt

WORKDIR /code
CMD ["true"]
