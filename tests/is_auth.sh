#!/usr/bin/bash
source curl_env

RES=$(curl -s -X GET ${URL}:${PORT}${BASE_PATH}/secure/auth/ \
    -H "${CONTENT_TYPE}" \
    -H "Authorization: Bearer ${JWT}")
echo "${bold}${blue}you are: ${green}${RES}"
