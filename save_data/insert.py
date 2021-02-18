import pymysql

id = '1001'
name = 'Bob'
age = 20
db = pymysql.connect(host='localhost', user='root',
                     password='ycysql', port=3306, db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
info = 'INSERT INTO students(id, name, age) VALUES (%s, %s, %s)'
try:
    cursor.execute(info, (id, name, age))
    db.commit()
except:
    db.rollback()
db.close()
