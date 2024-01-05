FROM python:3.10.13-slim-bullseye

# Set python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONF8=1 \
    PIP_NO_CACHE_DIR=off

# Update OS and install software
RUN apt-get update -y \
    && apt-get upgrade -y \
    && python -m pip install --upgrade pip

RUN apt-get install -y git
RUN apt-get install -y make
RUN apt-get update -y \
    && apt install -y gcc

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt
COPY .bashrc /root/