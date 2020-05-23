# вариант 1
# имя БД
DATABASE_NAME = 'mydatabase.db'
# имя(имена) таблиц
NAME_TABLE = ['employees', 'patients', 'accident']
# столбцы
COLUMN_TYPE = {
	'employees' : [
		(0, 'full_name', 'varchar(50)', 1, None, 0),
		(1, 'position', 'varchar(30)', 1, None, 0),
		(2, 'height', 'tinyint unsigned', 0, None, 0),
		(3, 'weight', 'FLOAT', 0, None, 0),
	],
	'patients' : [
		(0, 'full_name', 'varchar(50)', 1, None, 0),
		(1, 'diagnosis', 'varchar(40)', 1, None, 0),
		(2, 'height', 'tinyint unsigned', 1, None, 0),
		(3, 'weight', 'FLOAT', 1, None, 0),
	],
	'accident' : [
		(0, 'date', 'DATETIME', 1, None, 0),
		(1, 'full_name_injured', 'varchar(50)', 1, None, 0),
		(2, 'full_name_', 'initiator varchar(50)', 1, None, 0),
		(3, 'degree_of_damage', 'varchar(3)', 1, None, 0),
		(4, 'start_data_healing', 'DATETIME', 1, 'current_timestamp', 0),
		(5, 'healing_period', 'DATETIME', 1, None, 0),
	],
}
