"""analysis.py is used to calculate the change in root motion."""
import maya.cmds as mc;

class Analyze(object):
	"""class Analyze is used to calculate the change in RootMotion values.:"""
	dataTest_Analyze = None;
	def Calculate(rm, scaleAmount):
		"""Calculate the root motion data after scaling."""
		print ("Calculate(rm, scaleAmount)");