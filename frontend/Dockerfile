# Set the base image
FROM python:3.12.4

# Install system dependencies for numpy/scipy
RUN apt-get update && apt-get install -y libopenblas-dev && apt-get clean

# Copy the requirements.txt into a tmp directory
COPY requirements.txt /tmp/requirements.txt

# Upgrade pip and install requirements
RUN python -m pip install --no-cache-dir --upgrade pip &&\
    python -m pip install --no-cache-dir --timeout 300000 -r /tmp/requirements.txt

# Copy the entire project
COPY . /app 

# Set up Project working directory
WORKDIR /app

# Expose Port
EXPOSE 7000

# Run the application
CMD ["streamlit", "run", "🏠_Home.py", "--server.port", "7000"]
