# Use the official Python 3.11 image as a parent image
FROM python:3.11-slim-bullseye

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app directory contents into the container at /app
COPY app /app

# Copy the data directory into the container at /app/data
COPY data /app/data

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the command to start the Flask app
CMD ["python3", "main.py"]
