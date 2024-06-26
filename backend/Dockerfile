# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install ODBC Driver 18 for SQL Server
RUN apt-get update \
    && apt-get install -y gnupg2 curl \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Set the working directory in the container
WORKDIR /backend

# Copy the current directory contents into the container at /backend

COPY . /backend 

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
