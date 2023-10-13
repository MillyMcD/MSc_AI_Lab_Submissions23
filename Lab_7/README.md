# Lab Seven README
## Virtual environment

To perform this lab, I used a virtual environment on my macbook. To get virtualenv, I pip installed in the terminal
```
pip3 install virtualenv
```
I then created a virtual environment `mongodb_lab` by doing
```
virtualenv mongodb_lab
```
Once created I activated my env by doing
```
source mongodb_lab/bin/activate
```
Then I pip installed two python libraries: jupyternotebook and pymongo
```
pip3 install notebook
pip3 install pymongo
```
Finally, I ran a jupyter notebook server on port 9001 on my local machine using the command
```
jupyter notebook --ip 0.0.0.0 --port 9001 --no-browser --allow-root
```
I then went to localhost:9001 in my browser and copied the token from the terminal as the password


To run this example end to end follow instructions 4 - 25 then run every cell in the notebook and then run birthdays_mongo.py
