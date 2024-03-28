#!/bin/bash
#to take url and then GET it
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
