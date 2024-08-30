# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Create the target directory inside the container
RUN mkdir -p /opt/render/project/src/

# Set the working directory inside the container
WORKDIR /opt/render/project/src/

# Copy all files from your local directory to the working directory in the container
COPY . /opt/render/project/src/

# Install any dependencies needed by your app (if using Flask or any framework)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port to access the app
EXPOSE 80

# Run the application when the container starts
CMD ["python", "imgapp.py"]
