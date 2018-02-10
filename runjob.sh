#!/bin/bash

cd `dirname $0`
source venv/bin/activate
python backblaze_stats_reader.py

