# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /nse_data

# Copy the requirements file into the container at /app
COPY requirements.txt /nse_data/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /nse_data/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define command to run the application
# Run the command to start the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "nse_data.wsgi:application"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
