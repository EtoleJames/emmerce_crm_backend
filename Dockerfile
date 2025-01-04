# Pull official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000 for Django
EXPOSE 8000

# Start the server
CMD ["gunicorn", "emmerce_crm_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
