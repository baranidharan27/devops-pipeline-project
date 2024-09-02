# Use the official Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY src/ /app/

# Install the dependencies
COPY src/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run the application
CMD ["python", "app.py"]
