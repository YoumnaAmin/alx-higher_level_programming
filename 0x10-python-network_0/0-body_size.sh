#!/bin/bash
# to take url and then GET it
URL=$1
curl -sI $URL | awk '/Content-Length/ {print $2}'
