import os

def playAudio():
	os.system('aplay -d 2 /home/pi/Documents/SolderStationAuto/Development/20seconds_sine.wav')
