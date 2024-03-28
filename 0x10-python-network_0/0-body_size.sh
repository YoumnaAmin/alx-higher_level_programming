#!/bin/bash
# to take url and then GET it
if [ $# -eq 1 ];
then
URL=$1
curl -sI $URL | awk '/Content-Length/ {print $2}'
fi
