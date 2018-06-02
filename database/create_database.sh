#!/bin/bash
# Author      : github.com/TonyChG
# Date        : Tue 15 May 2018 05:47:15 PM CEST
# Version     : 0.0.1
# Description : Create database

# SQL Credentials
database="knockknock"
username="root"
password="root"
port="3306"
host="127.0.0.1"

# SQL files
target="."


tables="$(ls -1 "$target/"*.sql)"

for table in $tables; do
  mysql -P $port -h $host -u"$username" -p"$password" "$database"< "$table" \
    || echo "ERR: $table" >2 && echo "Success: $table"
done

