#!/bin/bash

# Navigate to the root directory of the application
cd $HOME/site/wwwroot

# Activate the Python virtual environment (if applicable)
# If you're using a virtual environment, replace '/path/to/venv' with the actual path
source /backend/fastapitest/.venv/scripts/activate

# Run the gunicorn command
gunicorn -w 1 -b 0.0.0.0:7000 backend.fastapitest.app:app
