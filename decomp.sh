#!/bin/sh

password=$(cat password)

echo "Unpacking pictures"
7z e -p$password -opictures pictures.7z

echo "Done"
