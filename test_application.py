from Development.DatabaseQuery.database_connect import *
from Development.Tests.Get_Serial_Number import *
from Development.Tests.play_Audio import *

def test_database_connect():
	assert database_connect() != -99

def test_getSerialNumber():
	cursor = database_connect()
	assert getSerialNumber(cursor, '' , '123') == '0'
	assert getSerialNumber(cursor, '79BBDJZZPAD' , '123') == '0109506058'
	assert getSerialNumber(cursor, '79BBDJZZJAB' , '123') == '0109506059'
	assert getSerialNumber(cursor, '79BBDJZZLAD' , '123') == '0109506060'
	assert getSerialNumber(cursor, '79BBDKBBFAB' , '123') == '0109506061'
	assert getSerialNumber(cursor, '79BBDJZZMAC' , '123') == '0109506062'
	assert getSerialNumber(cursor, '79BBDJZZFAC' , '123') == '0109506063'
	assert getSerialNumber(cursor, '79BBDJZZJAD' , '123') == '0109506064'
	assert getSerialNumber(cursor, '79bbdjzzfaD' , '123') == '0109506065'
	assert getSerialNumber(cursor, '' , '123') == '0'

def test_playAudio():
	assert playAudio() != '0'