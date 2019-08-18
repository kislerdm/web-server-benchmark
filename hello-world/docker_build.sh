#!/bin/bash

BASE=${PWD}/py

for i in $(ls -d ${BASE}/*); do
  echo ${i}
  cd ${i}
  docker build -t hello-world:py_$(basename ${i}) .
done