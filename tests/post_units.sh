#!/usr/bin/bash
source curl_env

RES=$(curl -s -X POST ${URL}:${PORT}${BASE_PATH}/secure/units/ \
    -H "${CONTENT_TYPE}" \
    -H "Authorization: Bearer ${JWT}" \
    -d '{"label":"ol_ou"}')
echo "${bold}${blue}Organisation unit created: ${normal}"
echo $RES | jq '.'
