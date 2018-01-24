import maya.cmds as mc;

# Make a basic cube, whatever dimensions you choose (default size is fine).
cube = mc.polyCube();
# Make a "controller" that moves the car along the x/z space by 
# rotating the cube you just made in two dimensions.
# Hint: You'll be connecting the car's x/z translation 
# to the cube's x/z rotation. A demo of this behavior using the 
# connectAttr() function can be found on p.42 of your book.
# Save your file as 'control_car.py'

import maya.cmds as mc;

# Make a basic cube, whatever dimensions you choose (default size is fine).
#print mc.help('move');
cube = mc.polyCube()[0];
mc.move(0, 0, -4, cube, relative=True);
# Make a "controller" that moves the car along the x/z space by 
# rotating the cube you just made in two dimensions.

mc.connectAttr(cube+'.rz','test_car'+'.translateX');
mc.connectAttr(cube+'.rx','test_car'+'.translateZ');
