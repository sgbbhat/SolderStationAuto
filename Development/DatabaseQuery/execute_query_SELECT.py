
def execute_query_SELECT(handle, selQuery, dbTable):
	handle.execute("Select ? from ?", selQuery, dbTable)
	queryResult = cursor.fetchall()
	return queryResult
