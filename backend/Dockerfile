# Use Python 3.10
FROM python:3.10

# Set working dicrectory
WORKDIR /app

# Copy the requirments file
COPY requirments.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirments.txt

# Copy the res of the application files
COPY . .

# Run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]