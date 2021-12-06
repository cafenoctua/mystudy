FROM python:3.9.9-slim-buster

# install ubuntu basic tools.
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
  sudo git wget cmake nano vim gcc g++ build-essential ca-certificates software-properties-common \
  && rm -rf /var/lib/apt/lists/*

# install python library
COPY ./project/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# config and clean up
RUN ldconfig \
  && apt-get clean \
  && apt-get autoremove