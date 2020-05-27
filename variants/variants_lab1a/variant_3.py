# вариант 3
# имя БД
DATABASE_NAME = 'mydatabase.db'
# имя(имена) таблиц
NAME_TABLE = ['employee_data', 'construction_objects', 'work_data']
# столбцы
COLUMN_TYPE = {
	'employee_data' : [
		(0, 'id', 'INTEGER', 1, None, 0),
		(1, 'name_employee', 'TEXT', 1, None, 0),
		(2, 'citizenship', 'TEXT', 0, None, 0),
		(3, 'end_permission', 'DATETIME', 0, None, 0),
		(4, 'position', 'TEXT', 0, None, 0),
		(5, 'tariff_rate', 'REAL', 0, None, 0),
	],
	'construction_objects' : [
		(0, 'id', 'INTEGER', 1, None, 0),
		(1, 'name_object', 'TEXT', 0, None, 0),
		(2, 'city', 'TEXT', 0, None, 0),
		(3, 'type_financing', 'TEXT', 0, None, 0),
		(4, 'start_date', 'DATETIME', 0, None, 0),
		(5, 'deadline', 'DATETIME', 0, None, 0),
	],
	'work_data' : [
		(0, 'id', 'INTEGER', 1, None, 0),
		(1, 'name_work', 'TEXT', 1, None, 0),
		(2, 'work_description', 'TEXT', 0, None, 0),
		(3, 'name_employee', 'TEXT', 1, None, 0),
		(4, 'number_hours', 'INTEGER', 0, None, 0),
	],
}
