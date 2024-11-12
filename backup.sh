#!/bin/bash

source /Users/mary/Desktop/finalSO/venv/bin/activate

/Users/mary/Desktop/finalSO/venv/bin/python /Users/mary/Desktop/finalSO/upload.py

echo "Backup completed at $(date)" >> /Users/mary/Desktop/backup2.log
