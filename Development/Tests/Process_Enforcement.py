# Process_Enforcement
from tkinter import END
import re
from Tests.displayResult import displayResult

def Process_Enforcement(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	# Running a stored procedure - getFlowKey
	getFlowKeyParam = (Sln, (modelFileContent['Part_No'])[0])
	databaseHandle.execute("{CALL [dbo].[getFlowKey] (?, ?)}", getFlowKeyParam)
	try:
		ProcessFlowKey = ((databaseHandle.fetchall())[0])[0]
	except:
		ProcessFlowKey = 1
	databaseHandle.commit()

	# Running a stored procedure - getProcessStep
	CurrentPartNumber = (modelFileContent['Part_No'])[0]
	CurrentProcessStep = re.sub(r"(\w)([A-Z])", r"\1 \2", (modelFileContent['Current_Step'])[0])

	getProcessStepParam = (ProcessFlowKey, CurrentProcessStep, CurrentPartNumber)
	databaseHandle.execute("{CALL [dbo].[getProcessStep] (?, ?, ?)}", getProcessStepParam)

	getProcessStepReturn = databaseHandle.fetchall()
	try:
		ProcessStep = (getProcessStepReturn[0])[0]
		PrePartNumber = (getProcessStepReturn[0])[1]
	except:
		ProcessStep = ''
		PrePartNumber = ''		
	databaseHandle.commit()

	# Checking if the unit is passed using the stored procedure - IsUnitPassed
	retResult = ''
	IsUnitPassedParam = (ProcessStep, PrePartNumber, Sln, retResult)
	databaseHandle.execute("{CALL [dbo].[IsUnitPassed] (?, ?, ?, ?)}", IsUnitPassedParam)
	IsUnitPassedReturn = int((databaseHandle.fetchall()[0])[0])
	databaseHandle.commit()

	if IsUnitPassedReturn == 1:
		result = "Pass"
		measurement = 1
	else:
		result = "Fail"
		measurement = 0

	mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)

	# Display test results
	displayResult(TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, mod_TestName, val, measurement, result)

	# Return test results
	if result == "Fail":
		return True
	else:
		return True

