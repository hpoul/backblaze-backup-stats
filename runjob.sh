#!/bin/bash

cd `dirname $0`
source venv/bin/activate
mkdir -p var
python backblaze_stats_reader.py >> var/job.log 2>&1

