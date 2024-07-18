Contents
==
- [Contents](#contents)
- [Docker](#docker)
- [Dockerfile example](#dockerfile-example)

<!--intro-start-->
# Docker
Docker is a platform designed to make it easier to create, deploy, and run applications by using containers.


- **Dockerfile** - A Dockerfile is a text file that contains instructions for building a Docker image.
- **Docker image** - An image is a read-only template that contains a set of instructions for creating a container.
- **Container** - A container is a lightweight, standalone, executable package that includes everything needed to run a piece of software, including the code, runtime, system tools, system libraries, and settings.

# Dockerfile example
Below is an example of a simple Dockerfile:

```
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

COPY guide/07_model_deployment/01_docker/test_script.py /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run script.py when the container launches
CMD ["python", "guide/07_model_deployment/01_docker/test_script.py"]
```

<!--intro-end-->
