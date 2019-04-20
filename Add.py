import pymsql.connector

db = pymysql.connector.connect("localhost", "user", "password", "database")
curser = db.curser()

def add_doc():
  file = open("document", 'r')
  file_content = file.read()
  file.close()
  query = "INSERT INTO table VALUES (%s)"
  cursor.execute(query, (file_content,))
  db.commit()
  db.close()
