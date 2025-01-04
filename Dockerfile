# Dockerfile
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Set the entry point to run the server
CMD ["gunicorn", "emmerce_crm_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
