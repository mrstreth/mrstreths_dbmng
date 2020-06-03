from peewee import *

DATABASE_NAME = 'mydatabase.db'

db = SqliteDatabase(DATABASE_NAME)

class agents_data(Model):
    id = IntegerField()
    name_agent = TextField()
    birthday_agent = DateTimeField(null=True)
    experience = FloatField(null=True)

    class Meta:
        database = db
        table_name = 'agents_data'

class policyholders_data(Model):
    id = IntegerField()
    name_policyholder = TextField()
    birthday_policyholder = DateTimeField(null=True)
    gender = TextField(null=True)
    nationality = TextField(null=True)
    type_insurance = TextField()
    date_insurance = DateTimeField()
    city_insurance = TextField(null=True)

    class Meta:
        database = db
        table_name = 'policyholders_data'

class cases_data(Model):
    id = IntegerField()
    name_policyholder = TextField()
    refund_amount = FloatField()
    number_policy = IntegerField()
    prize_amount = FloatField()
    policyholders_amount = FloatField()

    class Meta:
        database = db
        table_name = 'cases_data'

db.connect()
db.create_tables([agents_data, policyholders_data, cases_data])
db.commit()
db.close()
