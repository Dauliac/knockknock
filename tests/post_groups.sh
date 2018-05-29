#!/usr/bin/bash
source curl_env

RES=$(curl -s -X POST ${URL}:${PORT}${BASE_PATH}/secure/groups/ \
    -H "${CONTENT_TYPE}" \
    -H "Authorization: Bearer ${JWT}" \
    -d '{"label":"ol_group"}')
echo "${bold}${blue}Group created: ${normal}"
echo $RES | jq '.'
