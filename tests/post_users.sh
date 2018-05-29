#!/usr/bin/bash
source curl_env

RES=$(curl -s -X POST ${URL}:${PORT}${BASE_PATH}/secure/users/ \
    -H "${CONTENT_TYPE}" \
    -H "Authorization: Bearer ${JWT}" \
    -d '{"email":"user@olcorp.com",
         "name":"olcorp",
         "lastname":"olcorp"}')
echo "${bold}${blue}Users list: ${normal}"
echo $RES | jq '.'
