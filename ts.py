#!/usr/bin/python
#
from datetime import datetime

run = False

while True:
    cron = '00:01'
    d = datetime.strptime(cron, "%H:%M")

    if not run:
        if datetime.today().hour < str(d).split(':')[0] and datetime.today().minute < str(d).split(':')[1]:
            run = True
            print "cron date"
            print d
            print datetime.today()
