# Backblaze Backup Statistics Tracker

Simple python script to read status of Backblaze (Personal) backup 
and log it into a CSV file for later tracking.

Currently only works on mac, because it reads data from /Library/Backblaze.bzpkg/bzdata


## Usage

    # 1. create virtualenv
    virtualenv venv
    source venv/bin/activate
    
    # 2. Install requirements
    pip -r requirements.txt
    
    # 3. Install cronjob
    crontab -e
    # Add the following line: (replace $INSTALLDIR)
    * * * * * 	$INSTALLDIR/runjob.sh

    # 4. Generate graph
    python plot.py
