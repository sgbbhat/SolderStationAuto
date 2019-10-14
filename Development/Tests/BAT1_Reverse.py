# Function measures battery voltage 
from tkinter import END
from os import *
import time 
import re
from Tests.displayResult import displayResult
from tkinter import messagebox 


def BAT1_Reverse(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	measurement = popen('megaio 0 ropto 8').read()
	mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)

	result = 'Pass' if float(measurement) == float(val[1]) else 'Fail'

	# Display tests and results
	displayResult(TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, mod_TestName, val, float(measurement), result)
	# Return test results
	
	if int(measurement) == 1 :
            messagebox.showerror("Error", "Battery 1 connected in Reverse")
	
	if int(measurement) == 1 :
		return False
	else:
		return True
