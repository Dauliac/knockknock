#!/bin/bash
# github/TonyChG

function exit_err {
    echo $1 >&2
    cd $pos
    exit 4
}
pos=$PWD

newuser="knockknock"
newgroups="video,sudo,audio,users"
uv4l_url="http://www.linux-projects.org/listing/uv4l_repo/lpkey.asc"
uv4l_deb="deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/strech strech main"

test $(id -u) -eq 0 || exit_err "Permission denied (need root priviliege)"
echo "Updating System"
curl $uv4l_url | sudo apt-key add - || exit_err "ERROR: Adding key for webrtc"
echo $uv4l_deb >> /etc/apt/sources.list || exit_err "ERROR: Adding deb to sources.list"
apt-get -y update && apt-get -y upgrade || exit_err "ERROR: Update"
apt-get -y install motion uv4l uv4l-raspicam || exit_err "ERROR: Motion install"

echo "Create user"
adduser $newuser || exit_err "ERROR: Cannot create $newuser"
usermod -a -G $newgroups $newuser || exit_err "ERROR: Adding $newuser to groups"

