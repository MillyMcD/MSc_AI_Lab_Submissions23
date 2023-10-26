#!/bin/bash

#create a virtual environment
virtualenv pulsar_classification_env

#source the virtual environment so you can jump in to it
source pulsar_classification_env/bin/activate

#now we pip install all of our packages
#this is done by using a requirements.txt file which stores them all
pip3 install --upgrade -r requirements.txt

#now run the setup to demonstrate this project, get the dataset into mongo and create authentication.
python3 create_mongo_auth.py

#now deactivate, our environment is ready for use
deactivate