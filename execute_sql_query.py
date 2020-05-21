import sqlite3
import os

DATABASE_NAME = 'mydatabase.db'
QUERY_FILE_NAME = 'gar_lab1a_0.txt'

if os.path.exists(DATABASE_NAME):
    os.remove(DATABASE_NAME)

try:
    conn = sqlite3.connect(DATABASE_NAME)
    file = open(QUERY_FILE_NAME, 'r')
    query = file.read()
    conn.execute(query)
except:
    print('error')
    # тут ошибка
finally:
    conn.commit()
    conn.close()