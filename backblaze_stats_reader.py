#!/usr/bin/python
import csv

import time
import xmltodict

bb = {
    'baseDir': '/Library/Backblaze.bzpkg/bzdata',
    'reportsDir': 'bzreports'
}

def bbfile(filename):
    tmp = '/'.join([bb['baseDir'], bb['reportsDir'], filename])
    print("file: %s" % tmp)
    return tmp

def parse_statistics():
    totals = {}
    remaining = {}
    with open(bbfile('bzstat_totalbackup.xml'), 'rb') as f:
        totalbackup = xmltodict.parse(f)
        xml_totals = totalbackup['contents']['totals']
        totals['files'] = xml_totals['@totnumfilesforbackup']
        totals['bytes'] = xml_totals['@totnumbytesforbackup']

    with open(bbfile('bzstat_remainingbackup.xml'), 'rb') as f:
        progress_backup = xmltodict.parse(f)
        xml_remaining = progress_backup['contents']['remaining']
        remaining['files'] = xml_remaining['@remainingnumfilesforbackup']
        remaining['bytes'] = xml_remaining['@remainingnumbytesforbackup']

    with open('backblaze_stats.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            time.time(),
            totals['files'],
            totals['bytes'],
            remaining['files'],
            remaining['bytes']
        ])

parse_statistics()
