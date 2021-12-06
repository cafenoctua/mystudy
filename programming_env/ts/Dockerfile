FROM node:14

ENV USER=app

ENV SUBDIR=appDir

RUN useradd --user-group --create-home --shell /bin/false $USER &&\
	npm install --global tsc-watch npm ntypescript typescript gulp-cli

ENV HOME=/home/$USER

COPY package.json gulpfile.js $HOME/$SUBDIR/

RUN chown -R $USER:$USER $HOME/*

USER $USER

WORKDIR $HOME/$SUBDIR

RUN npm install

CMD ["node", "dist/index.js"]
