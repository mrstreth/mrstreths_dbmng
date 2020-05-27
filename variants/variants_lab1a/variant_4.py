# вариант 4
# имя БД
DATABASE_NAME = 'mydatabase.db'
# имя(имена) таблиц
NAME_TABLE = ['details_data', 'invoice_data', 'order_data']
# столбцы
COLUMN_TYPE = {
	'details_data' : [
		(0, 'id', 'INTEGER', 1, None, 0),
		(1, 'number_detail', 'INTEGER', 1, None, 0),
		(2, 'manufacturer', 'TEXT', 0, None, 0),
		(3, 'name_rus', 'TEXT', 0, None, 0),
		(4, 'name_eng', 'TEXT', 0, None, 0),
		(5, 'weight', 'REAL', 1, None, 0),
		(6, 'type', 'TEXT', 1, None, 0),
		(7, 'price', 'REAL', 1, None, 0),
		(8, 'warehouse', 'TEXT', 1, None, 0),
		(9, 'quantity', 'INTEGER', 1, None, 0),
	],
	'invoice_data' : [
		(0, 'id', 'INTEGER', 1, None, 0),
		(1, 'invoice_number', 'INTEGER', 1, None, 0),
		(2, 'date_sale', 'DATETIME', 1, None, 0),
		(3, 'warehouse_sale', 'TEXT', 1, None, 0),
		(4, 'quantity', 'INTEGER', 1, None, 0),
	],
	'order_data' : [
		(0, 'id', 'INTEGER', 1, None, 0),
		(1, 'order_date', 'DATETIME', 1, None, 0),
		(2, 'order_list', 'TEXT', 1, None, 0),
		(3, 'warehouse_loading', 'TEXT', 0, None, 0),
		(4, 'delivery_date', 'DATETIME', 0, None, 0),
		(5, 'warehouse_delivery', 'TEXT', 0, None, 0),
		(6, 'quantity', 'INTEGER', 1, None, 0),
	],
}
