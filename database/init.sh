#!/bin/bash
# Author      : github.com/TonyChG
# Date        : Sat 02 Jun 2018 01:08:37 PM CEST
# Version     : 0.0.1
# Description :

IMG_NAME="test_knockknock_db"
CONTAINER_NAME="knockknock_db"

USERNAME="admin"
DATABASE="knockknock"
PASSWORD="password"

docker ps -a | grep -q $CONTAINER_NAME \
  && docker rm -f $CONTAINER_NAME
docker build -t $IMG_NAME `dirname $0` \
  && docker run --name $CONTAINER_NAME -p 3306:3306 -d $IMG_NAME \
  && docker logs -f $CONTAINER_NAME
