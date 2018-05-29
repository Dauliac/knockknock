#!/usr/bin/bash
source curl_env
JWT=$(curl -X POST ${URL}:${PORT}${BASE_PATH})
    # -d 'email=olcorp_auth
        # password=olcorp')
echo "${bold}${blue}Your jwt is:${green} ${JWT}"
# sed -i -e 's/JWT=.*/JWT='$JWT'/g' curl_env
