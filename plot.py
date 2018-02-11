#!/usr/bin/python

import plotly
import plotly.graph_objs as go

from datetime import datetime

import csv

x = list()
y = list()
totalbytes = list()
remainingfiles = list()

with open('backblaze_stats.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        date = datetime.fromtimestamp(float(row[0]))
        x.append(date)
        # remaining bytes.
        y.append(int(row[4]))
        totalbytes.append(int(row[2]))
        remainingfiles.append(int(row[3]))

data = [
    go.Scatter(x=x, y=y, yaxis='y'),
    go.Scatter(x=x, y=totalbytes),
    go.Scatter(x=x, y=remainingfiles, yaxis='y2', name='Remaining Files')
]
plotly.offline.plot({
    "data": data,
    "layout": go.Layout(
        title="Testing",
        yaxis=dict(
            title='Y1',
        ),
        yaxis2=dict(
            title='Y2',
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
