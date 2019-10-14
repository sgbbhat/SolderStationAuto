# Function to measure battery voltage and display test 
from tkinter import END
from os import *
import time 
import re
from Tests.displayResult import displayResult
from tkinter import messagebox 

def BAT2_Voltage(root, key, val, databaseHandle, mfgID,Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	rawScale = popen('megaioind 0 ruin 3').read()
	measurement = float(rawScale)
	result = 'Pass' if measurement > float(val[1]) and measurement < float(val[2]) else 'Fail'

	mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)

	# Display Test and results
	displayResult(TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, mod_TestName, val, measurement, result)
	
	Bat2Reverse = popen('megaioind 0 optread 7').read()
	if int(Bat2Reverse) == 1 :
            messagebox.showerror("Error", "Battery 2 connected in Reverse")

	# Return test results
	if result == "Fail" or int(Bat2Reverse) == 1 :
		return False
	else:
		return True
