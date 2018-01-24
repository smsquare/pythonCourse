#!/bin/bash

currDir=${PWD##*/}

#Ensure that the person is running the file from the PythonProject root folder
reqDir="PythonProject"

#If you are in the correct folder then the .bash_profile file will be located here
file="_MAC_PYTHON_REF_/.bash_profile"
dest="~/.bash_profile"

if [ "$currDir" = "$reqDir" ]
then
	echo "Init: In proper directory"
else
	echo "ERROR: 'PythonProject' MUST be current working directory."
fi

if [-f "$file"]
then
	echo "$file found."
else
	echo "ERROR: $file not found."
fi
