#!/usr/bin/python

import csv

import datetime

with open('backblaze_datastudio.csv', 'w', newline='') as out:
    writer = csv.writer(out)
    writer.writerow(['date', 'totalfiles', 'totalbytes', 'remainingfiles', 'remainingbytes'])
    with open('backblaze_stats.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            date = datetime.datetime.fromtimestamp(float(row[0]))
            row[0] = date.strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow(row)
