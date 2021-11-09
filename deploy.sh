#!/bin/bash

sudo apt install python3 python3-pip python3-venv gunicorn3 -y

#python3 -m venv venv
#source venv/bin/activate

pip3 install -r requirements.txt

#while getops "c" options; do
#    case ${options} in
#        c) create=true;;
#    esac
#done

#if [ ${create}]; then
#    python create.py
#fi


#python3 app.py

#python3 -m pytest --cov=application
python3 -m pytest --cov=Fives --cov-report html
python3 Fives.py
