#!/bin/bash

# Navigate to the root directory of the application
cd $HOME/site/wwwroot

# Activate the Python virtual environment (if applicable)
source /backend/fastapi/.venv/bin/activate

# Run the Python program
python /backend/fastapitest/main.py