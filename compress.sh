#!/bin/sh

mkdir pictures

echo "Resizing/compressing pictures"
for img in picture-links/*;
do 
	new_img=pictures/$(basename $img)
	convert $img -define jpeg:extent=500kb -resize 50% jpg:$new_img
done

password=$(cat password)

echo "Archiving pictures"
7z a -p$password pictures.7z pictures/

rm -rf pictures

echo "Done"
