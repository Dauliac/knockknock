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
test $(id -u) -eq 0 || exit_err "Permission denied (need root priviliege)"
echo "Updating System"
apt-get -y update && apt-get -y upgrade || exit_err "ERROR: Update"
apt-get -y install motion || exit_err "ERROR: Motion install"

echo "Create user"
adduser $newuser || exit_err "ERROR: Cannot create $newuser"
usermod -a -G $newgroups $newuser || exit_err "ERROR: Adding $newuser to groups"

