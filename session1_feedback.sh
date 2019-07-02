#!/bin/bash
echo "Starting student number $1"
echo "Starting session1, saving to file $1_session1_feedback.txt"

python ./sander/feedback_nao1/session1.py | tee ./sander/logs/$1_session1_feedback.txt

echo "Finished session1."
