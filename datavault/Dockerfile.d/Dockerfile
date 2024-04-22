FROM python:3.11.9

# Updated OS and pip
RUN apt update -y \
    && apt -y upgrade \
    && python -m pip install --upgrade pip

# Install Tools
RUN apt install -y \
    git \
    make

# Install Python library
COPY ./Dockerfile.d/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Set bashrc
COPY ./Dockerfile.d/.bashrc /root/