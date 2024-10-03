# Use Python 3.12.1 slim as a base image
FROM python:3.12.1-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire FastAPI app and data.db into the container
COPY ./ ./

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
