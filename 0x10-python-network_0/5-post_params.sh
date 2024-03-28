#!/bin/bash
#to take url and then GET it
curl -s -X POST -d "email=test%40gmail.com&subject=I will%20always%20be%20here%20for%20PLD" "$1"
