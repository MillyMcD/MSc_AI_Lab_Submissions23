#!/bin/bash

#sourcing our environment
source review_classification_env/bin/activate

#creating a jupyter notebook server
jupyter notebook --ip 0.0.0.0 --port 9241 --no-browser --allow-root &