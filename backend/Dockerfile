# backend/Dockerfile

# ============================================
# THEORY: Dockerfile Instructions
#
# FROM: Base image to build upon
# ENV: Set environment variables
# WORKDIR: Set working directory in container
# RUN: Execute commands during build
# COPY: Copy files from host to container
# EXPOSE: Document which port the app uses
# CMD: Command to run when container starts
# ============================================

# Use Python 3.11 slim image (smaller size)
FROM python:3.11-slim

# Prevent Python from writing bytecode files
ENV PYTHONDONTWRITEBYTECODE=1
# Ensure Python output is sent directly to terminal
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies for PostgreSQL
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Start server with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "backend.wsgi:application"]