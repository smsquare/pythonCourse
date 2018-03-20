import maya.cmds as mc;
def TranslateZ(amountToScale):
	"""TranslateZ of the root by amountToScale. Use percentage from 0.0-2.0"""
	objs = mc.ls(sl=True);
	obj = objs[0];
	animAttr = mc.listAnimatable(obj);
	animAttrIndex = 0;
	for attr in animAttr:
		numKeyFrames = mc.keyframe(attr, query=True, keyframeCount=True);
		if (attr == u'|root.translateZ'):
		   times = mc.keyframe(attr, query=True, index=(0,numKeyFrames), timeChange=True);
		   values = mc.keyframe(attr, query=True, index=(0,numKeyFrames), valueChange=True);
		   for i in range(0,numKeyFrames):
			   mc.setKeyframe(obj + '.translateZ', value=values[i] * amountToScale, time=times[i]);