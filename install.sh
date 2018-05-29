#!/bin/bash
# Author      : github.com/TonyChG
# Date        : Tue 15 May 2018 06:05:55 PM CEST
# Version     : 0.0.1
# Description : Install script for knockknock

# Constants

# Configs
python_version="3.5"
newuser="knockknock"
newgroups="video,sudo,audio,users"
mode="dev"

# Init
source_list="/etc/apt/sources.list"
uv4l_key_url="http://www.linux-projects.org/listing/uv4l_repo/lrkey.asc"
uv4l_deb="deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/stretch stretch main"
pydir="Python-3.6.5.tar.xz"
dependencies=( "uv4l" "uv4l-raspicam" "ffmpeg" "uv4l-tc358743-extras" "uv4l-server" )

function exit_err {
  echo "ERROR!: $1" >&2
  exit 42
}

# Init Tasks
function install {
  test $(id -u) -eq 0 || exit_err "Permission denied. (Need sudo privilieges)"
  adduser --disabled-password --gecos "" $newuser || exit_err "Can't create user $newuser"
  usermod -a -G "$newgroups" "$newuser" || exit_err "Fail to add $newuser to $newgroups"
  curl http://www.linux-projects.org/listing/uv4l_repo/lrkey.asc | apt-key add -
  sed -i.orig -e '' "$source_list" \
    && echo "$uv4l_deb" >> "$source_list" || exit_err "Adding uv4l deb"
      apt-get update && apt-get upgrade -qy || exit_err "Update pi fail."
      apt-get install -qy --allow-unauthenticated "${dependencies[@]}" \
        || exit_err "Install dependencies"
  curl -sLO "https://www.python.org/ftp/python/3.6.5/$pydir"
  cd "$pydir"
  ./configure && make && make "test" && make install
  python3.6 -v
}

function remove {
  apt-get purge "${dependencies[@]}"
  test $(id -u) -eq 0 || exit_err "Permission denied. (Need sudo privilieges)"
  deluser --force --remove-home "$newuser" && deluser -g "$newuser" \
    || exit_err "Can't delete $newuser"
  cp "$source_list.orig" "$source_list"
}

function show_help {
  echo "## To remove totally knockknock"
  echo ">       ./install --remove"
  echo "## To install"
  echo ">       ./install --init"
}

case "$1" in
  "--remove") echo "Remove Knockknock server"; remove;;
  "--init") echo "Install Knockknock server."; install;;
  *) show_help;;
esac
