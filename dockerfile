# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
