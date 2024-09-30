#!/bin/bash
until [[ $bashrc == exit ]]
do
    read -p "enter a line to add to root's bahsrc: " bashrc
    if [[ $bashrc != "exit" ]];
    then
    echo $bashrc >> /root/.bashrc
    fi
done
