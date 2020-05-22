# вариант 0 - тестовый

# имя БД
DATABASE_NAME = 'mydatabase.db'

# имя(имена) таблиц
NAME_TABLE = ['employees']

# типы столбцов
COLUMN_TYPE = {  # правильное описание столбцов
        # SQL: PRAGMA table_info(имя_таблицы)
        'employees':
                [(0, 'id', 'INT UNSIGNED', 1, None, 0),
                (1, 'name', 'VARCHAR(20)', 1, None, 0),
                (2, 'birthday', 'DATETIME', 1, None, 0),
                (3, 'sex', 'VARCHAR(1)', 1, None, 0),
                (4, 'active', 'BOOL', 0, 'FALSE', 0),
                (5, 'salary', 'MEDIUMINT UNSIGNED', 1, None, 0)],
}