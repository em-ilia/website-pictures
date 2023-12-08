#!/bin/sh

password=$(cat password)

echo "Unpacking pictures"
7z x -p$password -opictures_tmp pictures.7z

echo "Done"
