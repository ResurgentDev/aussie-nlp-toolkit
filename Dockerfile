# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the repo into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose relevant ports (if needed later)
# eg. EXPOSE 8080

# Define the entrypoint for the container
ENTRYPOINT ["python", "main.py"]
