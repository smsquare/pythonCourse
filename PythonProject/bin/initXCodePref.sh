#!/bin/bash
file="../_MAC_PYTHON_REF_/Default.xccolortheme"
dest="/Users/student/Library/Developer/Xcode/UserData/FontAndColorThemes/Default.xccolortheme"
if [ -f "$file" ]
then
	echo "$file found."
	echo "Location of Xcode:  ~/Library/Developer/Xcode/UserData/FontAndColorThemes/"
	rm $dest
	cp -v $file $dest
else
	echo "$file not found!"
fi

