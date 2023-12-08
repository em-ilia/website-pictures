#!/bin/sh

WEBROOT=/usr/share/nginx/html/ilia.moe
DIRECTORY=$(realpath $(dirname $0))
cd $DIRECTORY

git stash
git stash clear
git pull --force origin main

./decomp.sh
sudo rm -rf $WEBROOT/pictures
sudo cp -r $DIRECTORY/pictures $WEBROOT/pictures
sudo mv $DIRECTORY/pictures_tmp/ $WEBROOT/pictures/img
rm -rf $DIRECTORY/pictures_tmp/
sudo chmod 707 $WEBROOT/pictures
sudo chmod 707 $WEBROOT/pictures/img
sudo python3 $DIRECTORY/image-fill.py $WEBROOT/pictures/index.html $WEBROOT/pictures/img
