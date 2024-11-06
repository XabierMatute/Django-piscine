#!/bin/bash

echo "pip version:"
pip --version

REPO_URL="https://github.com/jaraco/path.git"
INSTALL_DIR="local_lib"

echo "Installing path.py from $REPO_URL on $INSTALL_DIR"
if [ -d "$INSTALL_DIR" ]; then
    echo "The directory already exists. Overwriting..."
    rm -fr "$INSTALL_DIR"
fi

echo "Installing..."
pip install git+$REPO_URL --target="$INSTALL_DIR" > install.log 

if [ $? -eq 0 ]; then
    echo "Successfull installation"
    python3 my_program.py
else
    echo "An error ocurred. Check the log file install.log"
fi
