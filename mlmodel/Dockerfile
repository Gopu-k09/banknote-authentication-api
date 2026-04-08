FROM python:3.11-slim

WORKDIR /app

# Copy all necessary files
COPY requirements.txt .
COPY main.py .
COPY model.pkl .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
