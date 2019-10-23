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

def Info_Messagebox_After(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):		
	global cancelPressed
	global valChanged
	global currentState

	cancelPressed = True	
	top = Toplevel(master = root)
	top.geometry("%dx%d%+d%+d" % (500, 300,700,400))
	top.title("Waiting for user input...")
	top.resizable(0,0)

	msg = Message(top, text = "RESETS ARE HELD LOW, SOLDER LCD ONLY \n \n \nWHEN SOLDER IS COMPLETE, PRESS FINGER SWITCH TO MEASURE BATTERY VOLTAGES", width = 400, font=(50))
	msg.place(x=50,y=70)

	buttonCancel = Button(top, text = "Cancel", command = setcancelPressed)
	buttonCancel.place(x=200,y=220)
	
	top.attributes('-topmost', 'true')	
	root.update()

	while((int(valChanged == 0)) and (cancelPressed == True)):
		currentState = popen('megaioind 0 ropto 1').read()
		valChanged = compareState(currentState)
		top.update()
		continue
	time.sleep(0.5)	

	currentState = 0
	valChanged = 0
	if cancelPressed == False:
		top.destroy()
		return False
	else:
		top.destroy()
		return True
