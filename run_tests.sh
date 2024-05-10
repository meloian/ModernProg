#!/bin/bash 
set -e  

python3 -m unittest discover -s /app/lab1 -p 'test_*.py'
python3 -m unittest discover -s /app/lab2 -p 'test_*.py'
python3 -m unittest discover -s /app/lab3 -p 'test_*.py'