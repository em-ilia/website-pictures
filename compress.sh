#!/bin/sh

mkdir pictures_tmp

echo "Resizing/compressing pictures"
for folder in picture-links/*;
do
	mkdir pictures_tmp/$(basename $folder)
for img in $folder/*;
do 
	new_img=pictures_tmp/$(basename $folder)/$(basename $img)
	echo $new_img
	echo $img
	convert $img -define jpeg:extent=500kb -resize 50% jpg:$new_img
done
done

password=$(cat password)

echo "Archiving pictures"
rm pictures.7z
7z a -p$password pictures.7z ./pictures_tmp/*

rm -rf pictures_tmp

echo "Done"
