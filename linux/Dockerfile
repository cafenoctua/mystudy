FROM ubuntu:latest

RUN apt -y update \
&& apt -y upgrade \
&& apt install -y vim

RUN yes | unminimize

RUN apt install -y \
    man-db \
    manpages-posix \
    manpages-dev \
    manpages-posix-dev