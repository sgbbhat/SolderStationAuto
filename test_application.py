from Development.DatabaseQuery.database_connect import *

def test_database_connect():
	assert database_connect() != -99
