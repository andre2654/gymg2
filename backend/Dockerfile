FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . /app

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]