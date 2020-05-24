# это правильная выполненая работа
# нужна для создания тестов
from peewee import *

DATABASE_NAME = 'mydatabase.db'

db = SqliteDatabase(DATABASE_NAME)


class employees(Model):  # таблица "employees"
    id = IntegerField()
    name = TextField()
    birthday = DateTimeField(null=True)
    sex = TextField()
    active = BooleanField(null=True, default=False)
    salary = IntegerField()

    class Meta:
        database = db
        table_name = 'employees'

db.connect()
db.create_tables([employees])
db.commit()
db.close()
