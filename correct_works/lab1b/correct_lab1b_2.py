from peewee import *

DATABASE_NAME = 'mydatabase.db'

db = SqliteDatabase(DATABASE_NAME)

class employee_data(Model):
    id = IntegerField()
    name = TextField()
    data_revenue = FloatField(null=True)
    data_estate = TextField(null=True)

    class Meta:
        database = db
        table_name = 'employee_data'

class data_laws(Model):
    id = IntegerField()
    law_number = IntegerField()
    rights_section = IntegerField(null=True)
    title = TextField()
    who_nominated = TextField(null=True)
    who_corrected = TextField(null=True)
    votes_for =IntegerField()
    votes_againist = IntegerField()

    class Meta:
        database = db
        table_name = 'data_laws'

db.connect()
db.create_tables([employee_data, data_laws])
db.commit()
db.close()
