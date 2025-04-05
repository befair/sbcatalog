FROM node:current-alpine3.21

MAINTAINER Luca Ferroni "luca@befair.it"

COPY . /code/ui
RUN npm install -g $(cat /code/ui/deps/npm)

EXPOSE 5000
CMD ["harp", "/code", "--host", "0.0.0.0", "--port", "5000"]
