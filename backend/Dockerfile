# Set the base image
FROM python:3.12.4

# Copy the requirements.txt into a tmp directory
COPY requirements.txt /tmp/requirements.txt

# Upgrade pip and install requirements.txt
RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir --timeout 300000 -r /tmp/requirements.txt

# Copy the entire project
COPY . /app 

# Set up Project working directory
WORKDIR /app

# Expose Port
EXPOSE 8080

# Run the application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]
