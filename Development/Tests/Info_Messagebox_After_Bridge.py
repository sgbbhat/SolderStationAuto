from tkinter import *
from tkinter import messagebox
import time
from os import *

cancelPressed = True
currentState = 0
valChanged = 0

def compareState (current):
	global currentState
	if (int(current) == 0) :
		return 0
	else:
		currentState = 0
		return 1

def setcancelPressed():	
	global cancelPressed
	messagebox.showerror("Error", "Testing Aborted")
	cancelPressed = False
	pass

def Info_Messagebox_After_Bridge(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):		
	global cancelPressed
	global valChanged
	global currentState

	cancelPressed = True	
	top = Toplevel(master = root)
	top.geometry("%dx%d%+d%+d" % (290, 150,800,450))
	top.title("Waiting for user input...")
	top.resizable(0,0)

	msg = Message(top, text = "SOLDER THE BRIDGE, \n \nWHEN SOLDER IS COMPLETE, PRESS THE \nFINGER SWITCH TO CHECK THE ASSEMBLY.", width = 290)
	msg.place(x=10,y=10)

	buttonCancel = Button(top, text = "Cancel", command = setcancelPressed)
	buttonCancel.place(x=120,y=100)
	
	top.attributes('-topmost', 'true')	
	root.update()

	while((int(valChanged == 0)) and (cancelPressed == True)):
		currentState = popen('megaio 0 optread 1').read()
		valChanged = compareState(currentState)
		top.update()
		continue
	time.sleep(0.5)	

	# Release reset after soldering complete
	popen('megaioind 0 woc 1 0')
	time.sleep(0.5)
	popen('megaioind 0 woc 2 0')
	
	time.sleep(0.5)	

	currentState = 0
	valChanged = 0
	if cancelPressed == False:
		top.destroy()
		return False
	else:
		top.destroy()
		return True
