FROM python:3.9.12-slim-buster

RUN apt -y update &&\
    apt install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# WORKDIR /project