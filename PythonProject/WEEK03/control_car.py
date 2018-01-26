import maya.cmds as mc;

# Make a basic cube, whatever dimensions you choose (default size is fine).
cube = mc.polyCube()[0];
mc.move(0, 0, -4, cube, relative=True);
# Create a multiplyDivide node to control the scaling of the rotation to translation
mdX = mc.createNode('multiplyDivide');
# Make a "controller" that moves the car along the x space
mc.connectAttr(cube+'.rz',mdX+'.input1X');
mc.setAttr(mdX+'.input2X', 1.0/-45.0);
mc.connectAttr(mdX+'.outputX','test_car'+'.translateX');

# Create a multiplyDivide node to control the scaling of the rotation to translation
mdZ = mc.createNode('multiplyDivide');
# Make a "controller" that moves the car along the z space
mc.connectAttr(cube+'.rx',mdZ+'.input1X');
mc.setAttr(mdZ+'.input2X', 1.0/45.0);
mc.connectAttr(mdZ+'.outputX','test_car'+'.translateZ');

# Select the cube 
mc.select(cube);