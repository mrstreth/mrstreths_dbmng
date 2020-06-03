# вариант 1
# имя БД
DATABASE_NAME = 'mydatabase.db'
# имя(имена) таблиц
NAME_TABLE = ['employee_data', 'incident_data', 'patient_data']
# столбцы
COLUMN_TYPE = {
	'employee_data' : [
		(0, 'id', 'INTEGER', 1, None, 0),
		(1, 'name_employee', 'TEXT', 1, None, 0),
		(2, 'position', 'TEXT', 0, None, 0),
		(3, 'employee_growth', 'INTEGER', 0, None, 0),
		(4, 'employee_weight', 'REAL', 0, None, 0),
	],
	'incident_data' : [
		(0, 'id', 'INTEGER', 1, None, 0),
		(1, 'date_incident', 'DATETIME', 1, None, 0),
		(2, 'name_victim', 'TEXT', 1, None, 0),
		(3, 'name_initiator', 'INTEGER', 0, None, 0),
		(4, 'degree_damage', 'INTEGER', 0, None, 0),
		(5, 'damage', 'TEXT', 1, None, 0),
		(6, 'start_sick', 'DATETIME', 0, None, 0),
		(7, 'period_sick', 'INTEGER', 0, None, 0),
	],
	'patient_data' : [
		(0, 'id', 'INTEGER', 1, None, 0),
		(1, 'name_patient', 'TEXT', 1, None, 0),
		(2, 'position', 'TEXT', 0, None, 0),
		(3, 'patient_growth', 'INTEGER', 0, None, 0),
		(4, 'patient_weight', 'REAL', 0, None, 0),
	],
}
