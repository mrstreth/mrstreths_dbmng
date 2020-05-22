import sqlite3


def execute_query(QUERY, DATABASE_NAME):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        conn.executescript(QUERY)
    except:
        print('error')
        raise ValueError
        # тут должна быть ошибка
    finally:
        conn.commit()
        conn.close()
