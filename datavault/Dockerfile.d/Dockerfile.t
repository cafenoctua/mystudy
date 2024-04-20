FROM debian:trixie

# update os
# RUN apt-get update && apt-get install -y python3.10
RUN set -x \
    && apt -y update \
    && apt-get install -y software-properties-common \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt install -y --no-install-recommends \
        build-essential \
        curl \
        vim \
        python3 \
        python3-pip \
        python3-dev \
        && apt-get clean \
        && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/*

# RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

# パッケージをインストールするためのpipの設定を行います
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt /tmp/requirements.txt

RUN ln -s /usr/bin/python3 /usr/bin/python 

WORKDIR /work
# RUN python3.11 -m venv .venv \
#     && . .venv/bin/activate \
# RUN pip install -r /tmp/requirements.txt