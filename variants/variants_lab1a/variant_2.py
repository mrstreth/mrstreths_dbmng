# вариант 2
# имя БД
DATABASE_NAME = 'mydatabase.db'
# имя(имена) таблиц
NAME_TABLE = ['employee_data', 'data_laws']
# столбцы
COLUMN_TYPE = {
	'employee_data' : [
		(0, 'id', 'INTEGER', 1, None, 0),
		(1, 'name', 'TEXT', 1, None, 0),
		(2, 'data_revenue', 'REAL', 0, None, 0),
		(3, 'data_estate', 'TEXT', 0, None, 0),
	],
	'data_laws' : [
		(0, 'id', 'INTEGER', 1, None, 0),
		(1, 'law_number', 'INTEGER', 1, None, 0),
		(2, 'rights_section', 'INTEGER', 0, None, 0),
		(3, 'title', 'TEXT', 1, None, 0),
		(4, 'who_nominated', 'TEXT', 0, None, 0),
		(5, 'who_corrected', 'TEXT', 0, None, 0),
		(6, 'votes_for', 'INTEGER', 1, None, 0),
		(7, 'votes_againist', 'INTEGER', 1, None, 0),
	],
}
