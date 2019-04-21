import pymsql.connector

def getFile():
    fileName = request.form['document']

    db = pymysql.connect("localhost", "user", "password", "database")

with db:
        cursor = db.cursor()

        file = open(fileName,'r')
        file_content = file.read()
        file.close()

        query = "INSERT INTO table VALUES (%s)"
        cursor.execute(query, (file_content,))

        db.commit()
        db.close()
