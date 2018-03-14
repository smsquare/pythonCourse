"""data.py is used to parse the data of the Root Motion."""
import maya.cmds as mc;

class Parser(object):
	"""class Parser is used to handle getting and validating the initial info from RootMotion.:"""
	dataTest = None;
	def Read(rm):
		"""Read the root motion data."""
		print ("TestRead()");