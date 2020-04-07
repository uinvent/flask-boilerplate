#!/bin/sh

app="flask-boilerplate"
docker build -t ${app} .
docker run -d -p 8000:8088 --name=${app} -v $PWD:/src ${app}
