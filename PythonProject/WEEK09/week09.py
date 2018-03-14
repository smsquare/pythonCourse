import spikey;
selection = maya.cmds.ls(sl=True);
print(selection);
spikey.addSpikes(selection[0]);