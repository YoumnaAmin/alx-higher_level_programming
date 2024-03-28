#!/bin/bash
#to take url and then GET it
curl -sI "$1" | awk '/Content-Length/ {print $2}'
