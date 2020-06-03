# скрипт для автоматического создания
# данных тестов
# python3 make_test.py <правильное_решенное_задание>
# Пример: python3 make_test.py correct_lab1a_0.txt

import os
import shutil
import sqlite3
import sys

DATABASE_NAME = 'mydatabase.db'
LIST_EXISTING_WORK = [  # имя работы и что ожидаем получить
    ('lab1a', 'txt'),
    ('lab1b', 'py')
]

# очищаем рабочую среду - удаляем бд
if os.path.exists(DATABASE_NAME):
    os.remove(DATABASE_NAME)

# если передали не те аргументы
if len(sys.argv) != 2:
    print('len agrv != 2')
    raise AttributeError

name_correct_file = sys.argv[1]
script_name_without_type = name_correct_file.split('.')[0]
list_name_correct_file = name_correct_file.split('_')
is_correct_file = True if list_name_correct_file[0] == 'correct' else False
WORK = list_name_correct_file[1]
VARIANT = list_name_correct_file[2].split('.')[0]
type_file = list_name_correct_file[2].split('.')[1]

# если файл не начинается с correct
if not is_correct_file:
    print('is not correct file')
    raise FileNotFoundError

# если не существует такой лабораторной  работы
if (WORK, type_file) not in LIST_EXISTING_WORK:
    print('work not exist')
    raise FileNotFoundError

# находим нужный нам файл в директории
list_name_correct_file = list()
path = "correct_works/{WORK}/".format(WORK=WORK)
files = os.listdir(path)
for file in filter(lambda x: x == name_correct_file, files):
    list_name_correct_file.append(file)

# если не удалось найти файл
if list_name_correct_file is []:
    print('Файл не найден!')
    raise FileNotFoundError

# если файлов несколько то необходим один
if len(list_name_correct_file) > 1:
    print('Программа нашла несолько файлов! Необходим только один')
    print('Список найденных файлов:')
    print(list_name_correct_file)
    raise FileNotFoundError

# теперь составляем тест для опеределенной виды работы
if WORK == 'lab1a':
    # извлекаем sql запрос и выполняем его
    try:
        file = open(path + name_correct_file, 'r')
        query = file.read()
        file.close()
    except:
        print('файл не найден')
        raise FileNotFoundError
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        conn.executescript(query)
        conn.commit()
        conn.close()
    except:
        print('error')
        raise ValueError
    # извлекаем необходимые данные для теста
    NAME_TABLE = list()  # имя(имена) таблиц
    COLUMN_TYPE = dict()  # типы столбцов
    conn = sqlite3.connect(DATABASE_NAME)
    # извлекаем имя(имена) таблиц
    res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    NAME_TABLE = [name[0] for name in res]

    # извлекаем типы солбцов
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

elif WORK == 'lab1b':
    # выполняем скрпт
    from peewee import *
    сommand_import = 'import correct_works.{WORK}.{FILE}'.format(\
                     WORK=WORK, FILE=script_name_without_type)
    exec(сommand_import)
    # из созданной БД извлекаем данные (такие же как в lab1a но поменяется наименование типов)
    NAME_TABLE = list()  # имя(имена) таблиц
    COLUMN_TYPE = dict()  # типы столбцов
    conn = sqlite3.connect(DATABASE_NAME)
    # извлекаем имя(имена) таблиц
    res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    NAME_TABLE = [name[0] for name in res]

    # извлекаем типы солбцов
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

# перемещает тест в папку с тестами
if os.path.exists('variants/variants_{}/variant_{}.py'.format(WORK, VARIANT)):
    os.remove('variants/variants_{}/variant_{}.py'.format(WORK, VARIANT))
shutil.move(name_file_data_test, 'variants/variants_{}/'.format(WORK))
print('ok')

# очищаем рабочую среду после выполнения
if os.path.exists(DATABASE_NAME):
    os.remove(DATABASE_NAME)
