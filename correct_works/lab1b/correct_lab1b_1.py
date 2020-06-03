from peewee import *

DATABASE_NAME = 'mydatabase.db'

db = SqliteDatabase(DATABASE_NAME)

class employee_data(Model):
    id = IntegerField()
    name_employee = TextField()
    position = TextField(null=True)
    employee_growth = IntegerField(null=True)
    employee_weight = FloatField(null=True)

    class Meta:
        database = db
        table_name = 'employee_data'

class patient_data(Model):
    id = IntegerField()
    name_patient = TextField()
    position = TextField(null=True)
    patient_growth = IntegerField(null=True)
    patient_weight = FloatField(null=True)

    class Meta:
        database = db
        table_name = 'patient_data'

class incident_data(Model):
    id = IntegerField()
    date_incident = DateTimeField()
    name_victim = TextField()
    name_initiator = IntegerField(null=True)
    degree_damage = IntegerField(null=True)
    damage = TextField()
    start_sick = DateTimeField(null=True)
    period_sick = IntegerField(null=True)

    class Meta:
        database = db
        table_name = 'incident_data'

db.connect()
db.create_tables([employee_data, patient_data, incident_data])
db.commit()
db.close()
