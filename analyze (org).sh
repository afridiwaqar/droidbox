#!/bin/bash

apk_dir=/media/waqar/store/android-sdk/DroidBox_4.1.1/APKs/

i=0

for entry in "$apk_dir"/*.apk
echo entry >> apklist.txt
do
	apks[$i] = "$entry"
	echo "Initializing Analsis -> $entry"
	./droidbox.sh $entry 60
	((i++))
	echo "Done Analsis --> $entry"
done

