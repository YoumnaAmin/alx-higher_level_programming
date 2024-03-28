#!/bin/bash
# to take url and then GET it
if [ $# -eq 1 ];
then
URL=$1
curl -s -o /dev/null -w "%{size_download}\n" $URL
fi
