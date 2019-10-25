# Log_Test_Data_SQL
from tkinter import END
import datetime
from tkinter import messagebox 

def Log_Test_Data_SQL(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput):
	if OperationMode == 'Experiment' :
		OperationModeExp = 'E'
	elif OperationMode == 'Production' :
		OperationModeExp = 'P'

	# Running a stored procedure - getFlowKey
	getFlowKeyParam = (Sln, (modelFileContent['Part_No'])[0])
	databaseHandle.execute("{CALL [dbo].[getFlowKey] (?, ?)}", getFlowKeyParam)
	try:
		ProcessFlowKey_format = ((databaseHandle.fetchall())[0])[0]
	except:
		ProcessFlowKey_format = 1
	databaseHandle.commit()
		
	TestNameTextContent = TestNameText.get(1.0, END)
	MinLimitTextContent = MinLimitText.get(1.0, END)	
	MaxLimitTextContent = MaxLimitText.get(1.0, END)
	MeasurementTextContent = MeasurementText.get(1.0, END)
	searchResult = ResultText.get(1.0, END)
	indexsearchResult = searchResult.find("Fail", 0)
	if indexsearchResult == -1 :
		Passed = 1
	else:
		Passed = 0

	# Insert in to Test Events Table
	timeNow = datetime.datetime.now() 
	testEventParam = (Sln, mfgID, (modelFileContent['Part_No'])[0], 1 ,ProcessFlowKey_format, OperationModeExp, 546 , 1, "" , int(Passed), timeNow, OperationModeInput)
	databaseHandle.execute("{CALL [dbo].[insertTestEvent] (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}", testEventParam)
	TestEventKey = int(((databaseHandle.fetchall())[0])[0])
	databaseHandle.commit()

	# Insert in to Test Event Results
	for test, minlim, maxlim, meas, res in zip(TestNameTextContent.splitlines(), MinLimitTextContent.splitlines(), MaxLimitTextContent.splitlines(), MeasurementTextContent.splitlines(), searchResult.splitlines()) :
		if test == 'Name':
			pass
		else:
			getTestDefinitionKeyParam = (test)
			databaseHandle.execute("{CALL [dbo].[getTestDefinitionKey] (?)}", getTestDefinitionKeyParam)
			testDefKey = int(((databaseHandle.fetchall())[0])[0])
			databaseHandle.commit()

			if res == 'Pass' :
				logPass = 1
			else:
				logPass = 0
			testEventResultsParam = (TestEventKey, testDefKey, meas, minlim, maxlim, logPass)
			databaseHandle.execute("{CALL [dbo].[insertTestEventResult] (?, ?, ?, ?, ?, ?)}", testEventResultsParam)
			databaseHandle.commit()

	# Insert in to Component Traceability
	if LotNumvberInput == "" :
		pass
	else :
		vendor, PartNumber, Datecode = LotNumvberInput.split(',')
		param = (mfgID, vendor, PartNumber, Datecode )
		databaseHandle.execute("{CALL [dbo].[InsertComponentTraceability] (?, ?, ?, ?)}", param)
		databaseHandle.commit()

	#databaseHandle.execute("Select MfgSerialNumber from dbo.TestEvent WHERE TestEventKey = ?" , TestEventKey)
	#try:
	#	MfgIdReturned = (databaseHandle.fetchall()[0])[0]
	#except:
	#	MfgIdReturned = ''

	#if(MfgIdReturned != mfgID) or MfgIdReturned == '':	
	#	messagebox.showerror("Error", "Data Log Failed")
	#	returnResult = False
	#else:
	#	returnResult = True

	return 
		
