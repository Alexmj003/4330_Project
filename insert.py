from mysql.connector import MySQLConnection, Error
from database_config import read_db_config
 
def insert_document(name, filename, keywords):
    query = "INSERT INTO documents(name, filename, keywords) " \
            "VALUES(%s,%s,%s)"
    args = (name, filename, keywords)
 
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.executemany(query, args)
 
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
        

def main():
    n = input('Documnet name:')
    f = input('Filename:')
    k = input('TopKeywords')
    insert_document(n, f, k)

if __name__ == '__main__':
    main()