# Function measures battery voltage 
from tkinter import END
from os import *
import time 
import re
from Tests.displayResult import displayResult
from tkinter import messagebox 

def BAT1_Voltage(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	rawScale = popen('megaioind 0 ruin 2').read()
	measurement = float(rawScale)
	mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)

	result = 'Pass' if measurement > float(val[1]) and measurement < float(val[2]) else 'Fail'

	# Display tests and results
	displayResult(TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, mod_TestName, val, measurement, result)
	# Return test results
	
	Bat1Reverse = popen('megaioind 0 ropto 8').read()
	if int(Bat1Reverse) == 1 :
            messagebox.showerror("Error", "Battery 1 connected in Reverse")
	
	if result == "Fail" or int(Bat1Reverse) == 1 :
		return False
	else:
		return True
