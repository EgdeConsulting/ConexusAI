bash
#!/bin/bash

# Save the current directory
current_dir=$(pwd)

# Navigate to the directory containing the Python script
cd ./FastApiTest

# Run the Python script
python application.py

# Return to the original directory
cd "$current_dir"