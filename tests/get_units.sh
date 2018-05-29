#!/usr/bin/bash
source curl_env

RES=$(curl -s -X GET ${URL}:${PORT}${BASE_PATH}/secure/units/ \
    -H "${CONTENT_TYPE}" \
    -H "Authorization: Bearer ${JWT}")
echo "${bold}${blue}Groups list: ${normal}"
echo $RES | jq '.'
