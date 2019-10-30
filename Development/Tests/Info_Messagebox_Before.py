from tkinter import *
from tkinter import messagebox
import time
from os import *

cancelPressed = True
currentState = 0
valChanged = 0

def compareState (current):
	global currentState
	if (int(current) == False) :
		return 0
	else:
		currentState = 0
		return 1

def setcancelPressed():
	global cancelPressed
	messagebox.showerror(title = 'Error', message = "Test Aborted")
	cancelPressed = False
	pass

def Info_Messagebox_Before(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):		
	global cancelPressed
	global valChanged
	global currentState

	cancelPressed = True
	top = Toplevel(master = root)
	top.geometry("%dx%d%+d%+d" % (500, 300,700,400))
	top.title("Waiting for user input...")
	top.resizable(0,0)

	msg = Message(top, text = "LOAD THE BOARD & LCD ON TO THE FIXTURE\n\n\n    THEN PRESS FINGER SWITCH TO START", width = 400, font=(50))
	msg.place(x=50,y=70)

	buttonCancel = Button(top, text = "Cancel", command = setcancelPressed)
	buttonCancel.place(x=200,y=200)

	top.attributes('-topmost', 'true')	
	root.update()

	while((valChanged == 0)  and (cancelPressed == True)):
		currentState = popen('megaioind 0 ropto 1').read()
		valChanged = compareState(currentState)
		top.update()
	time.sleep(0.2)
	
	# Clamp
	
	time.sleep(1.0)

	# Hold Reset low while soldering 		
	popen('megaioind 2 woc 1 on')
	popen('megaioind 2 woc 2 on')

	currentState = 0
	valChanged = 0

	if cancelPressed == False:
		top.destroy()
		return False
	else:
		top.destroy()
		return True
