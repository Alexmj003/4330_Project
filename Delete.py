import pymsql.connector

def getFile():
    fileName = request.form['document']

    db = pymysql.connect("localhost", "user", "password", "database")

with db:
    curser = db.curser()

    query = "DELETE FROM table WHERE id ='%s'"
    cursor.execute(query);

    db.commit()
    db.close()
