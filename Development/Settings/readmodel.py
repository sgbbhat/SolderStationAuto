import re
from collections import OrderedDict

def readModel(filename):
	fhandle = open(filename, "r")
	testDict = OrderedDict()
	for line in fhandle:
		strline = str(line)
		strlinenew = re.sub(r'\s', '', strline)
		splitname = strlinenew.split(',')
		testDict[splitname[0]] = splitname[1:]
	return testDict
#for key, val in testDict.items():
#	print(key + " -> " + str(val))

#for key in testDict.items():
	
