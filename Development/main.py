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
		"ClampUp" : Clamp_Up,
		"ClampDown" : Clamp_Down,
                "VinVoltage" : Vin_Voltage,
		"ValidID":Valid_ID,
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

# Create a handle for Error Log
ErrorLogHandle = open(ErrorLog, "a")

# Window settings
root.title(StationName)
root.geometry("1130x750")
root.resizable(0,0)
root.configure(background='SlateGray4')

# Row#1 : Label to diplay model file heading - root, Lname, Ltext , Lheight,  Lwidth, Lrelief, Lbg, Lfg, Lfont, Lplacex, Lplacey
FilePathLabelTitle = CreateLabel(root, "FilePathLabelTitle",  "Model"  , 1,  13, "flat", 'SlateGray4' ,  'white' , ('Times', 12) , 18, 7)

# Row#1 : Label to Test Mode - root, Lname, Ltext , Lheight,  Lwidth, Lrelief, Lbg, Lfg, Lfont, Lplacex, Lplacey
FilePathLabelTitle = CreateLabel(root, "FilePathLabelTitle",  "Test Mode"  , 1,  13, "flat", 'SlateGray4' ,  'white' , ('Times', 12) , 18, 95)

# Row#1 : Label to Test Mode Comment - root, Lname, Ltext , Lheight,  Lwidth, Lrelief, Lbg, Lfg, Lfont, Lplacex, Lplacey
FilePathLabelTitle = CreateLabel(root, "FilePathLabelTitle",  "Comment"  , 1,  13, "flat", 'SlateGray4' ,  'white' , ('Times', 12) , 100, 95)

# Row#1 :  WasMfg Connection heading
WasMfgConnectionTitle = CreateLabel(root, "WasMfgConnectionTitle",  "WasMfg"  , 1,  8, "flat", 'SlateGray4' ,  'white' , ('Times', 12) , 1050, 7)

# Chose Experiment or Production Mode
tkvar = StringVar(root)
choises = {"Production", "Experiment"}
tkvar.set("Production")
OperationMode = OptionMenu(root, tkvar,  *choises)
OperationMode.place(x=21, y=120)
OperationMode.config(relief = "sunken", bd= 0)

# Entry widget for operation mode comment
OperationModeInput = Entry(root, bd = '3' , relief = "sunken", width=26, font=('Times', 21))
OperationModeInput.place(x=130, y=120)

# Entry widget for entering lot number
LotNumvberInput = Entry(root, bd = '3' , relief = "sunken", width=26, font=('Times', 21))
LotNumvberInput.place(x=725, y=120)

# Row#2 : Entry widget heading
MfgIDLabelTitle = CreateLabel(root, "MfgIDLabelTitle",  "Mfg. ID"  , 1,  12, "flat", 'SlateGray4' ,  'white' , ('Times', 12) , 20, 175)

# Row#2 : Messages Label heading
LastScannedLabelTitle = CreateLabel(root, "LastScannedLabelTitle",  "Last Scanned Mfg. ID"  , 1,  20, "flat", 'SlateGray4' ,  'white' , ('Times', 12) , 500, 175)

# Row#2 :  Messages Label heading
LastScannedSerialNumberTitle = CreateLabel(root, "LastScannedSerialNumberTitle",  "Serial Number"  , 1,  25, "flat", 'SlateGray4' ,  'white' , ('Times', 12) , 850, 175)

# Row#3 :  Label to diplay Messages heading
MessagesLabelTitle = CreateLabel(root, "MessagesLabelTitle",  "Select Model File & Scan Mfg.ID to Start..."  , 1,  100, "flat", 'SlateGray4' ,  'white' , ('Times', 12) , 20, 270)

# Row#2 : Battery Lot # heading
LotNumLabelTitle = CreateLabel(root, "LotNumLabelTitle",  "Battery Lot#", 1,  12, "flat", 'SlateGray4' ,  'white' , ('Times', 12) , 722, 95)

# Select model file Button 
SelectModelButtonImage = PhotoImage(file = 'SelectFile.png')
SelectModelButtonImageSub = SelectModelButtonImage.subsample(13,13)
SelectModelButton = Button(root, image=SelectModelButtonImageSub, bg = 'white', command = showDialogButton)
SelectModelButton.place(x=1000, y=32)

# Entry widget
mfgIdInput = Entry(root, bd = '2' , relief = "sunken", width=26, font=('Times', 21))
mfgIdInput.place(x=21, y=201)

# Connection to the database
databaseHandle = database_connect()
if databaseHandle == -99:
	WasMfgConnection = Canvas(root, height = 45, width = 45, bg = 'red' )
	ErrorLogHandle.write(str(datetime.datetime.now()) + " : " + "Failed to connect to the database\n")
else:
	WasMfgConnection = Canvas(root, height = 45, width = 45, bg = 'lime green' )
WasMfgConnection.place(x=1055, y=31)

# Field to diplay Serial Number
MessageDisplaySlNo = Label(root, text = "" , height = 2, width = 30, borderwidth = 3, relief = "sunken", justify = LEFT)
MessageDisplaySlNo.place(x=850, y=200)

# Field to diplay  Mfg ID 
MessageDisplayMfgID = Label(root, text = "" , height = 2, width = 30, borderwidth = 3, relief = "sunken", justify = LEFT)
MessageDisplayMfgID.place(x=500, y=200)

# Label to diplay model file name and location
FilePathLabel = Label(root, text = "" , height = 2, width = 120, borderwidth = 2, relief = "sunken")
FilePathLabel.place(x=20, y=33)

# Field to diplay TestName 
TestNameText = Text(root, height = 22, width = 40, bd = 1, relief = "sunken", bg = 'gray78')
TestNameText.configure(font = (12))
TestNameText.insert(INSERT, "Name" )
TestNameText.place(x=23, y=300)

# Field to diplay MinLimitText 
MinLimitText = Text(root, height = 22, width = 16, bd = 1, relief = "sunken", bg = 'gray78')
MinLimitText.configure(font = (12))
MinLimitText.insert(INSERT, "Min. Spec" )
MinLimitText.place(x=430, y=300)

# Field to diplay MaxLimitText
MaxLimitText = Text(root, height = 22, width = 16, bd = 1, relief = "sunken", bg = 'gray78')
MaxLimitText.configure(font = (12))
MaxLimitText.insert(INSERT, "Max. Spec" )
MaxLimitText.place(x=595, y=300)

# Field to diplay MeasurementText
MeasurementText = Text(root, height = 22, width = 16, bd = 1, relief = "sunken", bg = 'gray78')
MeasurementText.configure(font = (12))
MeasurementText.insert(INSERT, "Measurement" )
MeasurementText.place(x=760, y=300)

# Field to diplay ResultText
ResultText = Text(root, height = 22, width = 17, bd = 1, relief = "sunken", bg = 'gray78')
ResultText.configure(font = (12))
ResultText.insert(INSERT, "Result" )
ResultText.place(x=925, y=300)

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
			if val[0] == 'Action':
				mod_TestName = 'Waiting for user input...'
				pass
			else:
				mod_TestName = "Checking " + re.sub(r"(\w)([A-Z])", r"\1 \2", key) 
			MessagesLabelTitle.config(text = mod_TestName)
			testResult = Select_Test(key)(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OpMode, OpModeText, LotNumvber)
			root.update()
			if testResult == False:
				playAudio()
				Log_Test_Data_SQL(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OpMode, OpModeText, LotNumvber)
				Clamp_Up(root, key, val, databaseHandle, mfgID, Sln, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText, modelFileContent, testStartTime, OperationMode, OperationModeInput, LotNumvberInput)
				MessagesLabelTitle.config(text = "Waiting for user input...")
				messagebox.showerror("Error", "Test Failed")
				MessagesLabelTitle.config(text = "Waiting for user input - Scan Mfg.ID barcode to begin...")
				break
	MessagesLabelTitle.config(text = "Waiting for user input - Scan Mfg.ID barcode to begin...")

# Binding ENTER key event
root.bind('<Return>', startTest)

root.mainloop()

