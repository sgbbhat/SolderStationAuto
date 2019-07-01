# Function displays test results in on the user interface under "Messages Section"

from tkinter import END
from os import *
import time 
import re

def displayResult(TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, mod_TestName, val, measurement, result):	
	# Display Test Name
	TestNameText.insert(END, "\n")
	TestNameText.insert(END, mod_TestName)

	# Display Min Limit
	MinLimitText.insert(END, "\n")
	MinLimitText.insert(END, str(val[1]))

	# Display Max Limit
	MaxLimitText.insert(END, "\n")
	MaxLimitText.insert(END, str(val[2]))
	
	# Display Measurement
	MeasurementText.insert(END, "\n")
	MeasurementText.insert(END, round(measurement, 2))

	# Display Result
	ResultText.insert(END, "\n")
	ResultText.insert(END, result)
