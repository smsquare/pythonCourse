#!/bin/bash

currDir=${PWD##*/}

# Ensure that the person is running the file from the PythonProject root folderd
dirMustBe="PythonProject"

# If you are in the proper directory, then the file will be here
file="_MAC_PYTHON_REF_/Default.xccolortheme"
dest="/Users/student/Library/Developer/Xcode/UserData/FontAndColorThemes/Default.xccolortheme"

if [ "$currDir" = "$dirMustBe" ]
then
	echo "curr dir: $currDir is the correct location."
else 
	echo "You need to be in the PythonProject directory to run this file."
fi

if [ -f "$file" ]
then
	echo "$file found."
	echo "currDir: $currDir"
	rm $dest
	cp -v $file $dest
else
	echo "$file not found!"
fi

