#Verify_PN
from tkinter import END
import re
from os import *
import time 
from Tests.displayResult import displayResult

def Verify_PN(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	databaseHandle.execute("Select distinct ProcessFlowKey from dbo.TestEvent WHERE MfgSerialNumber = ? AND ProcessFlowKey != 0", mfgID)
	ProcessFlowKey = databaseHandle.fetchall()
	CurrentPartNumber = modelFileContent['Part_No']
	CurrentProcessStep = 'Board Test'
	databaseHandle.execute("Select PrePartNumber from dbo.ProcessEnforcementStep WHERE ProcessFlowKey = ? AND CurrentPartNumber = ? AND CurrentProcessStep = ?", int((ProcessFlowKey[0])[0]), CurrentPartNumber[0], CurrentProcessStep)
	PrePartNumber = databaseHandle.fetchall()
	if bool(PrePartNumber) == False:
		result = "Fail"
		measurement = 0
	elif (PrePartNumber[0])[0] == CurrentPartNumber[0] :
		result = "Pass"
		measurement = 1
	else:
		result = "Fail"
		measurement = 0

	mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)

	# Display test results
	displayResult(TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, mod_TestName, val, measurement, result)

	# Return test result
	if result == "Fail":
		return False
	else:
		return True
