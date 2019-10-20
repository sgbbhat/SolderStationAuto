# Function runs the stored procedure "getSerialNumber" taking Manufacturing Serial Number as input

def getSerialNumber(databaseHandle, mfgID, MessageDisplaySlNo):
	if mfgID == '':
		serialNumber = '0'
	else :
		databaseHandle.execute("{CALL [dbo].[getSerialNumber] (?)}", mfgID)
		try:
			serialNumber = ((databaseHandle.fetchall())[0])[0]
		except:
			serialNumber = '0'

		MessageDisplaySlNo.config(text = str(serialNumber), anchor = 'w')
		databaseHandle.commit()

	return serialNumber
