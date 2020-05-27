# вариант 0
# имя БД
DATABASE_NAME = 'mydatabase.db'
# имя(имена) таблиц
NAME_TABLE = ['employees']
# столбцы
COLUMN_TYPE = {
	'employees' : [
		(0, 'id', 'integer', 1, None, 0),
		(1, 'name', 'TEXT', 1, None, 0),
		(2, 'birthday', 'DATETIME', 0, None, 0),
		(3, 'sex', 'TEXT', 1, None, 0),
		(4, 'active', 'BOOLEAN', 0, 'FALSE', 0),
		(5, 'salary', 'INTEGER', 1, None, 0),
	],
}
