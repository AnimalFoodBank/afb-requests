# Dockerfile
# Pull base image
FROM python:3.11-slim-bookworm AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Use base image
FROM builder AS appenv

# Copy project
COPY . /code/

# Run entrypoint.sh
