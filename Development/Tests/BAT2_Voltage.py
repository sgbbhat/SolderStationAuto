# Function to measure battery voltage and display test 
from tkinter import END
from os import *
import time 
import re
from Tests.displayResult import displayResult
from tkinter import messagebox 

def BAT2_Voltage(root, key, val, databaseHandle, mfgID,Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	rawScale = popen('megaioind 0 ruin 2').read()
	measurement = float(rawScale)
	result = 'Pass' if measurement > float(val[1]) and measurement < float(val[2]) else 'Fail'

	mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)

	# Display Test and results
	displayResult(TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, mod_TestName, val, measurement, result)

	# Return test results
	if result == "Fail" :
		return False
	else:
		return True
