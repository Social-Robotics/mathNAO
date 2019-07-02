#!/bin/bash
echo "Starting student number $1"
echo "Starting session1, saving to file $1_session1_nofeedback.txt"

python ./sander/nofeedback_nao1/session1.py | tee ./sander/logs/$1_session1_nofeedback.txt

echo "Finished session1."
