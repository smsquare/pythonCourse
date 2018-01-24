import maya.cmds as mc;
# Create Sphere and Locator
sph = mc.polySphere()[0];
loc = mc.spaceLocator()[0];
# Connect the locator y-translate to sphere scale
mc.connectAttr(loc+'.ty', sph+'.scaleX');
mc.connectAttr(loc+'.ty', sph+'.scaleY');
mc.connectAttr(loc+'.ty', sph+'.scaleZ');