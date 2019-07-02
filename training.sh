#!/bin/bash

echo "Starting student number $1"
echo "Starting training, saving to file $1_training.txt"

python ./sander/training/training.py | tee ./sander/logs/$1_training.txt

echo "Finished training."