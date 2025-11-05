# Use a lightweight Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Copy dependency file first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Copy and prepare the startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Expose port (optional for documentation)
EXPOSE 5000

# Run the startup script
CMD ["/start.sh"]
