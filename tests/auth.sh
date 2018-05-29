#!/bin/bash
# Author      : github.com/TonyChG
# Date        : Tue 29 May 2018 11:04:39 AM CEST
# Version     : 0.0.1
# Description :

baseurl="http://0.0.0.0:5000/api"

loginform="email=admin@example.com&password=password"
res=$(curl -s -d "$loginform" "$baseurl/login")

if [ "" != "$res" ]; then
  token=$(echo "$res" | jq -r '.token')
  echo "Token: $token"
  res=$(curl -s -I -H "Authorization: $token" "$baseurl/authenticated" | head -1)
  echo "Response: $res"
else
  echo "Fail to login: $loginform"
fi
