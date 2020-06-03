from peewee import *

DATABASE_NAME = 'mydatabase.db'

db = SqliteDatabase(DATABASE_NAME)

class details_data(Model):
    id = IntegerField()
    number_detail = IntegerField()
    manufacturer = TextField(null=True)
    name_rus = TextField(null=True)
    name_eng = TextField(null=True)
    weight = FloatField()
    type = TextField()
    price = FloatField()
    warehouse = TextField()
    quantity = IntegerField()

    class Meta:
        database = db
        table_name = 'details_data'

class invoice_data(Model):
    id = IntegerField()
    invoice_number = IntegerField()
    date_sale = DateTimeField()
    warehouse_sale = TextField()
    quantity = IntegerField()

    class Meta:
        database = db
        table_name = 'invoice_data'

class order_data(Model):
    id = IntegerField()
    order_date = DateTimeField()
    order_list = TextField()
    warehouse_loading = TextField(null=True)
    delivery_date = DateTimeField(null=True)
    warehouse_delivery = TextField(null=True)
    quantity = IntegerField()

    class Meta:
        database = db
        table_name = 'order_data'

db.connect()
db.create_tables([details_data, invoice_data, order_data])
db.commit()
db.close()
