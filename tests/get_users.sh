#!/usr/bin/bash
source curl_env

RES=$(curl -s -X GET ${URL}:${PORT}${BASE_PATH}/secure/users/ \
    -H "${CONTENT_TYPE}" \
    -H "Authorization: Bearer ${JWT}")
echo "${bold}${blue}Users list: ${normal}"
echo $RES | jq '.'
