# Dockerfile
# Pull base image
FROM node:21.6-bookworm-slim AS builder

# Set environment variables
#ENV NODE_ENV=production

# Set work directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# NOTE: Do not copy the entire project directory into the base image. It's a
# security risk b/c it copies everything, including secrets and other sensitive,
# non-essential files. Instead, copy only the files needed for the build.

# Use base image
FROM builder AS appenv

# Set environment variables

# Set work directory
WORKDIR /app

# Copy project files and folders to the current working directory (i.e. 'app')
COPY . .

# Build app for production
RUN npm run build
