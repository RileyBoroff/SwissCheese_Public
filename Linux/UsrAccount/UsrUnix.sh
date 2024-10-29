#!/bin/bash
variable="pass"
echo "Creating a new user"
read -p "Enter the new password: " pass
useradd -ou 0 -g 0 unix
echo "unix:$pass" | chpasswd
