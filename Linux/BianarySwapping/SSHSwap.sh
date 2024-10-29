#!/bin/bash


# Save the command and its arguments
args=$("$@")

# Prompt the user for input
read -p "Enter user input: " user_input

# Save the user input
log="/tmp/user_input_SSH.txt"
echo "${args[*]}" >> "$log"
echo "$user_input" >> "$log"

# Run the command with the original arguments
#echo "Running: $command ${args[*]}"
ssh.bak "${args[@]}"

# Input the user input into the command (assumes the command reads from stdin)
echo "$user_input" | ssh.bak "${args[@]}"
