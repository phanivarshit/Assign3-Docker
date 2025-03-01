# Use a lightweight base image
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Install necessary dependencies and remove cache to reduce image size
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --no-cache-dir nltk \
    && apk del .build-deps

# Copy only the necessary files
COPY script.py /app/
COPY home/data /home/data/

# Set execute permissions for the script
RUN chmod +x /app/script.py

# Command to run the script
CMD ["python", "/app/script.py"]
