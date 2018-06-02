############################
# Date        : Sat 02 Jun 2018 12:53:01 PM CEST
# Version     : 0.0.1
# Description : 0.0.1
FROM mariadb

WORKDIR /data
ADD . /data

ENV MYSQL_RANDOM_ROOT_PASSWORD yes
ENV MYSQL_DATABASE knockknock
ENV MYSQL_USER admin
ENV MYSQL_PASSWORD password

EXPOSE 3306
