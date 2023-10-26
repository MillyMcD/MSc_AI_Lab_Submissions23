# Pulsar Prediction: Assessment README

This README guide is for linux and mac machines which have a shell/bash-like terminal. Make sure you have `virtualenv` installed on your machine.

This project uses a virtual environment for deployment. This keeps the host environment clean by not installing potentially conflicting packages. To install the virtual environment, call 

```
sh installation.sh
``` 

which will create a virtualenv called `pulsar_classification_env`. This will also use the `create_mongo_auth.py` script to add the `PulsarDataset.csv` into your running instance of MongoDB, before asking you to create a User. If the user is already defined, it will keep asking until your create a valid user.

Once installed, you can deploy the project by calling 

```
source run.sh
```

This will spin up a jupyter notebook server on port 9001, and the UI will spin up a short while after that.

