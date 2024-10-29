#!/bin/bash
#assign the variable
read -p "enter the alias name: " command
read -p "enter the commands for the alias to run: " alias
echo "alias $command='$alias'" >> /root/.bashrc
