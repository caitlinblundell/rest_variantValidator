FROM python:3.13-slim

 #Set the working directory inside the container
WORKDIR /app

# Update apt-get and install git (if needed)
RUN apt-get update && apt-get install -y git

# Upgrade pip
RUN pip install --upgrade pip

# Copy only requirements.txt first (for caching)
COPY requirements.txt .

# Install dependencies from requirements.txt if it exists
# Doing this before copying the rest of the project takes advantage of Docker layer caching
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Set the default command to run your Python app
# Replace 'my_awesome_app.py' with your script name
CMD ["python", "app.py"]

