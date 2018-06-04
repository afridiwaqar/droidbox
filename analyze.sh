#!/bin/bash

apk_dir=/media/waqar/store/android-sdk/DroidBox_4.1.1/APKs

i=0

apklist="$apk_dir"/apklist.txt

if [ ! -f "$apklist" ] ; then
	for entry in "$apk_dir"/*.apk; do
		echo "$entry" >> "$apk_dir"/apklist.txt
	done
fi

while IFS= read -r line
do
	echo "Launching Emulator..."
	./startemu.sh
	echo "Reading Line $line"
	./droidbox.sh "$line" 60
	sed -i -e "1d" "$apklist"
	echo "Killing Emulator..."
	pkill emulator
	echo "Done"

done <"$apklist"

if [ ! -s file ]; then
	echo "remvoing file"
	rm -f $apklist
fi

echo "All Done..."
