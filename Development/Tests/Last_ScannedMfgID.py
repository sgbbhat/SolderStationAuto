# Enter_Mfg_ID
from tkinter import END

def Last_ScannedMfgID(mfgIdInput, MessageDisplay, TestNameText, MinLimitText, MaxLimitText, MeasurementText, ResultText):
	mfgId = mfgIdInput.get()
	mfgIdInput.delete(0, 'end')
	MessageDisplay.config(anchor = 'w', text = str( mfgId))
	TestNameText.delete(2.0, END)
	MinLimitText.delete(2.0, END)
	MaxLimitText.delete(2.0, END)
	MeasurementText.delete(2.0, END)
	ResultText.delete(2.0, END)
	return mfgId
