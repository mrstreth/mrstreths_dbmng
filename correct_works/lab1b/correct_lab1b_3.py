from peewee import *

DATABASE_NAME = 'mydatabase.db'

db = SqliteDatabase(DATABASE_NAME)

class employee_data(Model):
    id = IntegerField()
    name_employee = TextField()
    citizenship = TextField(null=True)
    end_permission = DateTimeField(null=True)
    position = TextField(null=True)
    tariff_rate = FloatField(null=True)

    class Meta:
        database = db
        table_name = 'employee_data'

class construction_objects(Model):
    id = IntegerField()
    name_object = TextField(null=True)
    city = TextField(null=True)
    type_financing = TextField(null=True)
    start_date = DateTimeField(null=True)
    deadline = DateTimeField(null=True)

    class Meta:
        database = db
        table_name = 'construction_objects'

class work_data(Model):
    id = IntegerField()
    name_work = TextField()
    work_description = TextField(null=True)
    name_employee = TextField()
    number_hours = IntegerField(null=True)

    class Meta:
        database = db
        table_name = 'work_data'

db.connect()
db.create_tables([employee_data, construction_objects, work_data])
db.commit()
db.close()
