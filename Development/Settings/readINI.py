from configparser import ConfigParser

def readINI():
	# Instantiate 
	config = ConfigParser()
	configFilePath = r'/home/pi/Documents/SolderStationAuto/Station/System.ini'
	config.read(configFilePath)

	# Parse Existing File
	StationName =  config.get('station', "Station Name")
	ErrorLog = config.get('station', 'Error Log')
	ModelDirectory = config.get('station', 'Model Directory')

	return StationName, ErrorLog, ModelDirectory
