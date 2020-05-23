# скрипт для автоматического создания
# данных для теста test_lab1a.py
# результат сохранится в variants/variants_lab1a/variant_<номер варианта>


import os
import shutil
import sqlite3

DATABASE_NAME = 'mydatabase.db'

# находим нужный нам файл correct_lab1a_<номер варианта>.txt
list_name_correct_file = list()
files = os.listdir()
for file in filter(lambda x: x.startswith('correct_lab1a_'), files):
    list_name_correct_file.append(file)

if list_name_correct_file is []:
    print('Файл correct_lab1a_<номер варианта>.txt не найден!')
    raise FileNotFoundError

if len(list_name_correct_file) > 1:
    print('Программа нашла несолько файлов! Необходим только один')
    print('Список найденных файлов:')
    print(list_name_correct_file)
    raise FileNotFoundError

# ивлекаем полное имя файла
correct_file = list_name_correct_file[0]

# извлекаем из названия файла нужные данные
values_correct_file = correct_file.split('_')
VARIANT = values_correct_file[2].split('.')[0]  # вариант
WORK = values_correct_file[1]  # имя работы (lab1a)

# очищаем рабочую среду - удаляем бд
if os.path.exists(DATABASE_NAME):
    os.remove(DATABASE_NAME)

# извлекаем sql запрос и выполняем его
file = open(correct_file, 'r')
query = file.read()
file.close()
try:
    conn = sqlite3.connect(DATABASE_NAME)
    conn.executescript(query)
    conn.commit()
    conn.close()
    print('ok')
except:
    print('error')
    raise ValueError

# извлекаем необходимые данные для теста
NAME_TABLE = list()  # имя(имена) таблиц
COLUMN_TYPE = dict()  # типы столбцов

conn = sqlite3.connect(DATABASE_NAME)
res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
NAME_TABLE = [name[0] for name in res]

for table in NAME_TABLE:
    res = conn.execute("PRAGMA table_info({})".format(table))
    table_description = list()
    for i, column in enumerate(res):
        description_column = column
        table_description.append(description_column)
    COLUMN_TYPE[table] = table_description

# запись в файл variant_<номер варианта>.py
name_file_data_test = 'variant_{}.py'.format(VARIANT)
file = open(name_file_data_test, 'w')
print('# вариант {}'.format(VARIANT), file=file, sep='')
print('# имя БД', file=file, sep='')
print("DATABASE_NAME = '{}'".format(DATABASE_NAME), file=file, sep='')
print('# имя(имена) таблиц', file=file, sep='')
print('NAME_TABLE = {}'.format(NAME_TABLE), file=file, sep='')
print('# столбцы', file=file, sep='')
print('COLUMN_TYPE = {', file=file, sep='')
for table in COLUMN_TYPE:
    print("\t'{}' : [".format(table), file=file, sep='')
    for i, column in enumerate(COLUMN_TYPE[table]):
        print('\t\t{},'.format(COLUMN_TYPE[table][i]), file=file, sep='')
    print('\t],', file=file, sep='')
print('}', file=file, sep='')
file.close()

shutil.move(name_file_data_test, 'variants/variants_lab1a/')
print('ok')