# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container to /backend
WORKDIR /newmain

# Copy the current directory contents into the container at /backend
COPY /newmain .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80
EXPOSE 8000

# Define environment variable


# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
