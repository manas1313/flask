#!/bin/bash
app="docker.Flaskdockerapp"
docker build -t ${app} .
docker run -d -p 5736:80 \
  --name=${app} \
  -v $PWD:/app ${app}