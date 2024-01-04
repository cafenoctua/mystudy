# FROM python:3.11.7
# FROM python:3.8.12-slim-buster
FROM python:3.10.13-slim-bullseye

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get autoremove -y

# install neccesary libraries
RUN apt-get install -y gettext \
    libcurl4-gnutls-dev \
    libexpat1-dev \
    libghc-zlib-dev \
    libssl-dev \
    make \
    wget
    
# compile git
RUN wget https://github.com/git/git/archive/v2.30.0.tar.gz \
    && tar -xzf v2.30.0.tar.gz \
    && cd git-* \
    && make prefix=/usr/local all \
    && make prefix=/usr/local install

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt