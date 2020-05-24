# это работа студента

# здесь самое главное это описание класса таблиц

# мы извлекаем только эту информацию

from peewee import *

DATABASE_NAME = 'mydatabase.db'

db = SqliteDatabase(DATABASE_NAME)


class employees(Model):  # таблица "employees"
    id = IntegerField()
    name = TextField()
    birthday = DateTimeField(null=True) #  пусть здесь он забыл резрешить Null
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
