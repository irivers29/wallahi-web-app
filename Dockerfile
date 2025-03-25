# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set a working directory for the app
WORKDIR /app

# Copy requirements.txt first to leverage Docker's layer caching
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5009

# Define environment variable for Python
ENV PYTHONUNBUFFERED=1

# Run app.py when the container launches
CMD ["python", "app.py"]
