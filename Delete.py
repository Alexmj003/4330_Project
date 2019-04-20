import pymsql.connector

db = pymysql.connector.connect("localhost", "user", "password", "database")
curser = db.curser()

def delete_doc():
    query = "DELETE FROM table WHERE id ='%s'"
    cursor.execute(query);
    db.commit()
