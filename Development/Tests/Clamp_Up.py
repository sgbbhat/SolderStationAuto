# Function measures battery voltage 
from tkinter import END
from os import *
import time 
import re
from Tests.displayResult import displayResult
from tkinter import messagebox 

def Clamp_Up(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	# Bring the clamp down
	popen('megaioind 0 wrelay 1 off')
	# mod_TestName = re.sub(r"(\w)([A-Z])", r"\1 \2", key)