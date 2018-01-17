#!/bin/bash
file="../_MAC_PYTHON_REF_/Default.xccolortheme"
if [ -f "$file" ]
then
	echo "$file found."
else
	echo "$file not found!"
fi

