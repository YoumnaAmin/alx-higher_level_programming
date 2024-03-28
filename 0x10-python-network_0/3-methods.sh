#!/bin/bash
#to take url and then GET it
curl -s -X OPTIONS -i "$1" | awk '/^Allow:/ {print $2}'
