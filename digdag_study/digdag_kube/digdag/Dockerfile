FROM azul/zulu-openjdk:8

ENV DIGDAG_VERSION=0.10.2

# update and set timezone to Asia/Tokyo
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install locales curl && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

ENV TZ JST-9

RUN curl -o /usr/local/bin/digdag --create-dirs -L "https://dl.digdag.io/digdag-${DIGDAG_VERSION}" && \
    chmod +x /usr/local/bin/digdag && \
    apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* && \
    adduser --shell /sbin/nologin --disabled-password --gecos "" digdag

# Install gcloud
RUN apt-get -y update
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN apt-get install -y apt-transport-https ca-certificates gnupg
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
RUN apt-get -y update && apt-get install -y google-cloud-sdk


USER digdag

WORKDIR /home/digdag
COPY ./project/start.sh ./start.sh
COPY ./project/config .config/digdag/config

RUN alias digdag="java -jar /usr/local/bin/digdag"

EXPOSE 65432

ENTRYPOINT [ "sh", "start.sh" ]