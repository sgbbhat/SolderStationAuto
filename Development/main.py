#!/usr/bin/env python3

from Settings.import_module import *

def Select_Test(name):
	return {
		"VerifyPN" : Verify_PN, 
		"ProcessEnforcement" : Process_Enforcement,
		"Battery1Voltage" : BAT1_Voltage,
		"Battery2Voltage" : BAT2_Voltage,
		"Battery1Reverse" : BAT1_Reverse,
		"Battery2Reverse" : BAT2_Reverse,
		"Reset1VoltageLow" : RST1_Voltage_Low,
		"Reset2VoltageLow" : RST2_Voltage_Low,
		"Reset1VoltageHigh" : RST1_Voltage_High,
		"Reset2VoltageHigh" : RST2_Voltage_High,
		"StartupDetection" : Wakeup_Pulse,
		"SerialNumber" : Serial_Number, 
		"TestTime" : Test_Time, 
		"LogTestData_SQL" : Log_Test_Data_SQL,
		"InfoMessageboxBefore" : Info_Messagebox_Before, 
		"InfoMessageboxAfter" : Info_Messagebox_After,
                "InfoMessageboxAfterBridge" : Info_Messagebox_After_Bridge,
                "VinVoltage" : Vin_Voltage,
		}.get(name, defaultfun)

modelFileContent = OrderedDict()

def showDialogButton():
	global modelFileContent
	folder_path = filedialog.askopenfilename(initialdir = ModelDirectory , title = "Select Model File", filetypes = (("text files", "*.txt") , ("all files", "*.*")))
	FilePathLabel.config(anchor = 'w', text = folder_path)
	modelFilepath = FilePathLabel.cget("text")
	modelFileContent = readModel(modelFilepath)

root = Tk()

# Read INI file
StationName, ErrorLog, ModelDirectory = readINI()

# Error Log
ErrorLogHandle = open(ErrorLog, "a")

# Window settings
root.title(StationName)
root.geometry("650x500")
root.resizable(0,0)
root.configure(background='SlateGray4')

# Row#1 : Label to diplay model file heading
FilePathLabelTitle = CreateLabel(root, "FilePathLabelTitle",  "Model"  , 1,  12, "flat", 'SlateGray4' ,  'white' , ('Times', 11) , 18, 7)

# Row#1 :  WasMfg Connection heading
WasMfgConnectionTitle = CreateLabel(root, "WasMfgConnectionTitle",  "WasMfg"  , 1,  8, "flat", 'SlateGray4' ,  'white' , ('Times', 11) , 543, 7)

# Chose Experiment or Production Mode
tkvar = StringVar(root)
choises = {"Production", "Experiment"}
tkvar.set("Production")
OperationMode = OptionMenu(root, tkvar,  *choises)
OperationMode.place(x=21, y=90)
OperationMode.config(relief = "sunken", bd= 0)

# Entry widget for operation mode comment
OperationModeInput = Entry(root, bd = '3' , relief = "sunken")
OperationModeInput.place(x=130, y=92)

# Entry widget for entering lot number
LotNumvberInput = Entry(root, bd = '3' , relief = "sunken")
LotNumvberInput.place(x=415, y=92)

# Row#2 : Entry widget heading
MfgIDLabelTitle = CreateLabel(root, "MfgIDLabelTitle",  "Mfg. ID"  , 1,  12, "flat", 'SlateGray4' ,  'white' , ('Times', 11) , 18, 125)

# Row#2 : Messages Label heading
LastScannedLabelTitle = CreateLabel(root, "LastScannedLabelTitle",  "Last Scanned Mfg. ID"  , 1,  20, "flat", 'SlateGray4' ,  'white' , ('Times', 11) , 217, 125)

# Row#2 :  Messages Label heading
LastScannedSerialNumberTitle = CreateLabel(root, "LastScannedSerialNumberTitle",  "Serial Number"  , 1,  25, "flat", 'SlateGray4' ,  'white' , ('Times', 11) , 416, 125)

# Row#3 :  Label to diplay Messages heading
MessagesLabelTitle = CreateLabel(root, "MessagesLabelTitle",  "Select Model File & Scan Mfg.ID to Start..."  , 1,  90, "flat", 'SlateGray4' ,  'white' , ('Times', 11) , 18, 175)

# Row#2 : Battery Lot # heading
LotNumLabelTitle = CreateLabel(root, "LotNumLabelTitle",  "Battery Lot#", 1,  12, "flat", 'SlateGray4' ,  'white' , ('Times', 11) , 416, 70)

# Select model file Button 
SelectModelButtonImage = PhotoImage(file = 'SelectFile.png')
SelectModelButtonImageSub = SelectModelButtonImage.subsample(18,18)
SelectModelButton = Button(root, image=SelectModelButtonImageSub, bg = 'white', command = showDialogButton)
SelectModelButton.place(x=510, y=30)

# Entry widget
mfgIdInput = Entry(root, bd = '2' , relief = "sunken")
mfgIdInput.place(x=20, y=150)

# Connection to the database
databaseHandle = database_connect()
if databaseHandle == -99:
	WasMfgConnection = Canvas(root, height = 35, width = 35, bg = 'red' )
	ErrorLogHandle.write(str(datetime.datetime.now()) + " : " + "Failed to connect to the database\n")
else:
	WasMfgConnection = Canvas(root, height = 30, width = 30, bg = 'lime green' )
WasMfgConnection.place(x=548, y=31)

# Field to diplay Serial Number
MessageDisplaySlNo = Label(root, text = "" , height = 1, width = 20, borderwidth = 3, relief = "sunken", justify = LEFT)
MessageDisplaySlNo.place(x=415, y=149)

# Field to diplay  Mfg ID 
MessageDisplayMfgID = Label(root, text = "" , height = 1, width = 20, borderwidth = 3, relief = "sunken", justify = LEFT)
MessageDisplayMfgID.place(x=217, y=149)

# Label to diplay model file name and location
FilePathLabel = Label(root, text = "" , height = 2, width = 60, borderwidth = 2, relief = "sunken")
FilePathLabel.place(x=20, y=30)

# Field to diplay TestName 
TestNameText = Text(root, height = 15, width = 40, bd = 1, relief = "sunken", bg = 'gray78')
TestNameText.insert(INSERT, "Name" )
TestNameText.place(x=19, y=200)

# Field to diplay MinLimitText 
MinLimitText = Text(root, height = 15, width = 8, bd = 1, relief = "sunken", bg = 'gray78')
MinLimitText.insert(INSERT, "Min Spec" )
MinLimitText.place(x=300, y=200)

# Field to diplay MaxLimitText
MaxLimitText = Text(root, height = 15, width = 8, bd = 1, relief = "sunken", bg = 'gray78')
MaxLimitText.insert(INSERT, "Max Spec" )
MaxLimitText.place(x=360, y=200)

# Field to diplay MeasurementText
MeasurementText = Text(root, height = 15, width = 12, bd = 1, relief = "sunken", bg = 'gray78')
MeasurementText.insert(INSERT, "Measurement" )
MeasurementText.place(x=420, y=200)

# Field to diplay ResultText
ResultText = Text(root, height = 15, width = 10, bd = 1, relief = "sunken", bg = 'gray78')
ResultText.insert(INSERT, "Result" )
ResultText.place(x=505, y=200)

# Main program begins
def startTest(mfgID):
	testStartTime = time.time()
	mfgID = Last_ScannedMfgID(mfgIdInput, MessageDisplayMfgID, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText)
	Sln = getSerialNumber(databaseHandle, mfgID, MessageDisplaySlNo)
	OpMode = OperationMode.cget("text")
	OpModeText = OperationModeInput.get()
	LotNumvber = LotNumvberInput.get()
	global modelFileContent
	if(bool(modelFileContent) == False):
		messagebox.showerror("Error" , "Model file not selected")
	for key, val in modelFileContent.items():
		if key == "" or bool(val) == False or key == 'name':
			pass
		else:
			testResult = Select_Test(key)(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OpMode, OpModeText, LotNumvber)
			root.update()
			if testResult == False:
				messagebox.showerror("Error", "Test Failed")
				Log_Test_Data_SQL(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OpMode, OpModeText, LotNumvber)
				break

# Binding ENTER key event
root.bind('<Return>', startTest)

root.mainloop()

