############################
# Date        : Sat 02 Jun 2018 12:31:23 AM CEST
# Version     : 0.0.1
# Description : 0.0.1
FROM node:alpine

WORKDIR /webui
ADD . /webui

RUN npm install

ENTRYPOINT ["npm", "run", "build"]
