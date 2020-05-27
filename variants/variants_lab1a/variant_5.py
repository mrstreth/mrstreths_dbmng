# вариант 5
# имя БД
DATABASE_NAME = 'mydatabase.db'
# имя(имена) таблиц
NAME_TABLE = ['agents_data', 'policyholders_data', 'cases_data']
# столбцы
COLUMN_TYPE = {
	'agents_data' : [
		(0, 'id', 'INTEGER', 1, None, 0),
		(1, 'name_agent', 'TEXT', 1, None, 0),
		(2, 'birthday_agent', 'DATETIME', 0, None, 0),
		(3, 'experience', 'REAL', 0, None, 0),
	],
	'policyholders_data' : [
		(0, 'id', 'INTEGER', 1, None, 0),
		(1, 'name_policyholder', 'TEXT', 1, None, 0),
		(2, 'birthday_policyholder', 'DATETIME', 0, None, 0),
		(3, 'gender', 'TEXT', 0, None, 0),
		(4, 'nationality', 'TEXT', 0, None, 0),
		(5, 'type_insurance', 'TEXT', 1, None, 0),
		(6, 'date_insurance', 'DATETIME', 1, None, 0),
		(7, 'city_insurance', 'TEXT', 0, None, 0),
	],
	'cases_data' : [
		(0, 'id', 'INTEGER', 1, None, 0),
		(1, 'name_policyholder', 'TEXT', 1, None, 0),
		(2, 'refund_amount', 'REAL', 1, None, 0),
		(3, 'number_policy', 'INTEGER', 1, None, 0),
		(4, 'prize_amount', 'REAL', 1, None, 0),
		(5, 'policyholders_amount', 'REAL', 1, None, 0),
	],
}
