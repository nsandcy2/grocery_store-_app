import mysql.connector
__cnxn=None
def get_sql_connection():
    global __cnxn
    if __cnxn is None:
        __cnxn = mysql.connector.connect(user='root', password='Nsandcy143@',
                                host='127.0.0.1',
                                database='grocery_store')
    return __cnxn