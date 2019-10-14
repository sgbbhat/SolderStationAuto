# Function measures battery voltage 
from tkinter import END
from os import *
import time 
import re
from Tests.displayResult import displayResult
from tkinter import messagebox 

def Clamp_Down(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	# Bring the clamp down
	popen('megaioind 0 wrelay 1')
	mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)

	# Display tests and results
	# displayResult(TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, mod_TestName, val, measurement, result)
	# Return test results
	
	#Bat1Reverse = popen('megaioind 0 ropto 8').read()
	#if int(Bat1Reverse) == 1 :
        #   messagebox.showerror("Error", "Battery 1 connected in Reverse")
	
	#if result == "Fail" or int(Bat1Reverse) == 1 :
	#	return False
	#else:
	#	return True
