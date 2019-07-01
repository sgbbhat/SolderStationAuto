# Wakeup_Pulse
from tkinter import END
import re
from Tests.displayResult import displayResult

def Wakeup_Pulse(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	result = "Pass"
	mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)
	measurement = 1

	# Display test and tests
	displayResult(TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, mod_TestName, val, measurement, result)

	# Return test result
	if result == "Fail":
		return False
	else:
		return True
