#!/usr/bin/python

import plotly
import plotly.graph_objs as go

from datetime import datetime

import csv

x = list()
remaining_bytes = list()
totalbytes = list()
remainingfiles = list()

with open('backblaze_stats.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        date = datetime.fromtimestamp(float(row[0]))
        x.append(date)
        # remaining bytes.
        remaining_bytes.append(int(row[4]))
        totalbytes.append(int(row[2]))
        remainingfiles.append(int(row[3]))

data = [
    go.Scatter(x=x, y=remaining_bytes, yaxis='y', name='Remaining Bytes'),
    go.Scatter(x=x, y=totalbytes, name='Total Bytes'),
    go.Scatter(x=x, y=remainingfiles, yaxis='y2', name='Remaining Files')
]
plotly.offline.plot({
    "data": data,
    "layout": go.Layout(
        title="Backblaze Backup",
        yaxis=dict(
            title='Bytes',
        ),
        yaxis2=dict(
            title='Files',
            titlefont=dict(
                color='rgb(148, 103, 189)'
            ),
            tickfont=dict(
                color='rgb(148, 103, 189)'
            ),
            overlaying='y',
            side='right'
        )
    )
})
