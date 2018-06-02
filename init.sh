#!/bin/bash
# Author      : github.com/TonyChG
# Date        : Sat 02 Jun 2018 02:01:44 AM CEST
# Version     : 0.0.1
# Description :

STATIC="$PWD/api/webui/static:/usr/src/app/static"
INDEX="$PWD/api/webui/index.html:/usr/src/app/templates/index.html"

IMG_BUILD_NAME="vuebuild_img"
IMG_API_NAME="knockknock_img"
CONTAINER_API_NAME="knockknock_api"

case "$1" in
  remove)
    docker ps -a | grep -q "$CONTAINER_API_NAME" \
      && docker stop $CONTAINER_API_NAME && docker rm $CONTAINER_API_NAME
    docker rmi $IMG_BUILD_NAME
    docker rmi $IMG_API_NAME
    ;;
  build)
    docker build -t $IMG_BUILD_NAME webui
    docker build -t $IMG_API_NAME api
    ln -sf "$PWD/api/webui/static" "$PWD/api/app"
    ln -sf "$PWD/api/webui/index.html" "$PWD/api/app/templates"
    ;;
  run)
    docker run -it --rm -v $PWD/api/webui:/webui/dist $IMG_BUILD_NAME
    docker run -d --name $CONTAINER_API_NAME -p 8080:5000 -v $STATIC -v $INDEX $IMG_API_NAME
    ;;
  up)
    $0 remove && $0 build && $0 run \
      && docker logs -f $CONTAINER_API_NAME
    ;;
  *)
    >&2 echo "Usage: $0 {build|run|remove|up}"
esac

