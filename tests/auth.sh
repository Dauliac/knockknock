#!/bin/bash
# Author      : github.com/TonyChG
# Date        : Tue 29 May 2018 11:04:39 AM CEST
# Version     : 0.0.1
# Description :

source curl_env

RES=$(curl -s -X POST ${URL}:${PORT}${BASE_PATH}/secure/users/ \
    -H "${CONTENT_TYPE}" \
    -H "Authorization: Bearer ${JWT}" \
    -d '{"email":"user@olcorp.com",
         "name":"olcorp",
         "lastname":"olcorp"}')
echo "${bold}${blue}Users list: ${normal}"
echo $RES | jq '.'
