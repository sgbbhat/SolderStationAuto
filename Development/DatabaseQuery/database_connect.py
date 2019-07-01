import pyodbc

def database_connect():
	try:
		conn = pyodbc.connect('DRIVER={FreeTDS};Server=Waseca-db2;PORT=1433;DATABASE=WasMfg;UID=testpack;PWD=Itron2;TDS_Version=7.4;')
		cursor = conn.cursor()
		return cursor
	except:
		return -99