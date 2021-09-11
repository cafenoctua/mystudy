FROM ubuntu:16.04
RUN apt-get update # && apt-get install -y curl apt-transport-https
RUN apt-get update && apt-get install -y iputils-ping dnsutils curl apt-transport-https \
    sudo git wget cmake nano vim gcc g++ build-essential ca-certificates software-properties-common \
    && rm -rf /var/lib/apt/lists/*
# pyhon
# RUN apt-get install -y python python-pip
RUN add-apt-repository ppa:deadsnakes/ppa \
&& apt-get update \
&& apt-get install -y python3.6 \
&& wget -O ./get-pip.py https://bootstrap.pypa.io/get-pip.py \
&& python3.6 ./get-pip.py \
&& ln -s /usr/bin/python3.6 /usr/local/bin/python3 \
&& ln -s /usr/bin/python3.6 /usr/local/bin/python
RUN pip3 install --upgrade pip
RUN pip3 install kubernetes

COPY main.py /main.py

WORKDIR /
CMD python /main.py

