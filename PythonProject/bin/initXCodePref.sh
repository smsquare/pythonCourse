#!/bin/bash
currDir=${PWD##*/}
# Ensure that the person is running the file from the PythonProject root folderd
dirMustBe="PythonProject"

# If you are in the proper directory, then the file will be here
file="_MAC_PYTHON_REF_/CUSTOM.xccolortheme"
dest="~/Library/Developer/Xcode/UserData/FontAndColorThemes/Default.xccolortheme"

if [ "$currDir" = "$dirMustBe" ]
then
	echo "curr dir: $currDir is the correct location."
else 
	echo "You need to be in the PythonProject directory to run this file."
fi

if [ -f "$file" ]
then
	echo "$file found."
		
	if [ -f "$dest" ] 
	then
		echo "$dest file exists. Replacing now."
		cp -v $file $dest
	else
		echo "Default profile doesnt exist. Creating it now."
		mkdir ~/Library/Developer/Xcode/UserData/FontAndColorThemes/
		cp $file ~/Library/Developer/Xcode/UserData/FontAndColorThemes/
		mv ~/Library/Developer/Xcode/UserData/FontAndColorThemes/CUSTOM.xccolortheme /Users/student/Library/Developer/Xcode/UserData/FontAndColorThemes/Default.xccolortheme
	fi
else
	echo "$file not found!"
fi

