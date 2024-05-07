#!/bin/bash

# Create a Virtual Environment
python3 -m venv .venv

# Activate the Virtual Environment
source .venv/bin/activate

# Set the install.sh script to executable
chmod +x install.sh

# Run the install.sh script
./install.sh