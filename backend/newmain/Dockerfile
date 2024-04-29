# Use an official Python runtime as a parent image
FROM python:3.11.8

# Set the working directory in the container to /backend
WORKDIR /newmain

# Copy the current directory contents into the container at /backend
COPY . . 

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000
EXPOSE 80

# Define environment variable

WORKDIR /newmain

# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", port="80"]
