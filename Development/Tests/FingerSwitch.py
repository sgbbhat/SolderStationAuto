from os import *
import time

def compareState (current):
	global currentState
	if (int(current) == False) :
		return 0
	else:
		currentState = 0
		return 1

valChanged = 0
while(valChanged == 0):
	currentState = popen('megaioind 0 ropto 1').read()
	valChanged = compareState(currentState)
	time.sleep(0.2)
