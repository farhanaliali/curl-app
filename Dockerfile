FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY app.py .

# Install dependencies
RUN pip install flask requests

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

