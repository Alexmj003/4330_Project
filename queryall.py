from mysql.connector import MySQLConnection, Error
from database_config import read_db_config
 
 
def query_fetchall(output = str('output.txt')):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM documents")
        rows = cursor.fetchall()
        file = open(output,'w')
        file.write('Total Row(s): ' + cursor.rowcount + '\n')
        for row in rows:
            file.write(row + '\n')
        file.close()
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    query_fetchall()
