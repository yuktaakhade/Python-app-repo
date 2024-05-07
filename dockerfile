
FROM python:3.9-slim

# working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir Flask

# Expose the port the app runs on
EXPOSE 80

# Define environment variable
ENV FLASK_APP app.py

# Run flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
