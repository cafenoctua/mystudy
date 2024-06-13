from ubuntu:22.04

RUN apt-get update && \
  apt install -y mysql-server-8.0 -f

COPY my.cnf /etc/my.cnf
RUN service mysql start
COPY ./sql /work/sql
WORKDIR /work