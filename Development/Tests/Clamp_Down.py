# Function measures battery voltage 
from tkinter import END
from os import *
import time 
import re
from Tests.displayResult import displayResult
from tkinter import messagebox 

def Clamp_Down(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	popen('megaioind 0 wrelay 1 on')
	
	time.sleep(0.5)	

	clamp_1_State = popen('megaioind 2 ropto 1').read()
	clamp_2_State = popen('megaioind 2 ropto 2').read()
	print(clamp_1_State)

	result = 'Pass' if float(clamp_1_State) == 0.0 else 'Fail'

	if result == 'Pass':
		return True
	else:
		messagebox.showerror("Error", "Clamp not down \n Check air pressure")
		return False