import pytest
import sqlite3
import os

NAME_PARAMETERS_FILE = 'parameters.txt'

# считаем параметры из файла NAME_PARAMETERS_FILE
parameters_file = open(NAME_PARAMETERS_FILE, 'r')
parameters = dict([line.strip().split('=') for line in parameters_file.readlines()])

сommand_import = \
    'from variants.variants_{WORK}.variant_{VARIANT} import DATABASE_NAME, NAME_TABLE, COLUMN_TYPE'.format( \
        WORK=parameters['WORK'], VARIANT=parameters['VARIANT'], )
exec(сommand_import)

if parameters['IS_SCRIPT'] == 'True':
    from peewee import *
    сommand_import = 'import {AUTHOR}_{WORK}_{VARIANT}'.format( \
        AUTHOR=parameters['AUTHOR'], WORK=parameters['WORK'], VARIANT=parameters['VARIANT'])
    exec(сommand_import)

# тесты для 'lab1a'
if parameters['WORK'] == 'lab1a':
    """Тесты для lab1a"""


    def test_existDB():
        """удалось ли создать БД"""

        global DATABASE_NAME
        flag = True
        print(os.path)
        if not os.path.exists(DATABASE_NAME):
            flag = False
        assert flag


    def test_existNamedTable():
        """существует ли таблица(ы) с нужными именами"""

        global NAME_TABLE
        global DATABASE_NAME
        flag = True
        conn = sqlite3.connect(DATABASE_NAME)
        res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [name[0] for name in res]
        if not tables:
            flag = False
        else:
            for name in tables:
                if name not in NAME_TABLE:
                    flag = False
                    break
        conn.close()
        assert flag


    def test_type_column():
        """проверка имена и типов созданных столбцов в каждой таблицу"""

        global COLUMN_TYPE
        global DATABASE_NAME
        global NAME_TABLE
        conn = sqlite3.connect(DATABASE_NAME)
        flag = False
        for table in NAME_TABLE:
            res = conn.execute("PRAGMA table_info({})".format(table))
            for i, column in enumerate(res):
                flag = True
                description_column = list(column)
                # преобразование строк (команд) в верхний регистр:
                for i1, elem in enumerate(description_column):
                    if type(elem) == str:
                        description_column[i1] = description_column[i1].upper()

                correct_description_column = list(COLUMN_TYPE[table][i])
                # преобразование строк (команд) в верхний регистр:
                for i2, elem in enumerate(correct_description_column):
                    if type(elem) == str:
                        correct_description_column[i2] = correct_description_column[i2].upper()

                if description_column != correct_description_column:
                    flag = False
                    break
            if flag is False:
                break
        conn.close()
        assert flag

# тесты для 'lab1b'
elif parameters['WORK'] == 'lab1b':
    """Тесты для lab1b"""

    # from peewee import *

    db = SqliteDatabase(parameters['DATABASE_NAME'])
    db.connect()


    # for table in NAME_TABLE:
    #     сommand_import = 'from {}_lab1b_{} import {}'.format(\
    #         parameters['AUTHOR'], parameters['VARIANT'], table)
    #     exec(сommand_import)
    #     сommand_import = 'db.create_tables([{}])'.format(table)
    #     exec(сommand_import)

    def test_existDB():
        """удалось ли создать БД"""

        global DATABASE_NAME
        flag = True
        print(os.path)
        if not os.path.exists(DATABASE_NAME):
            flag = False
        assert flag


    def test_existNamedTable():
        """существует ли таблица(ы) с нужными именами"""

        global NAME_TABLE
        global DATABASE_NAME
        flag = True
        conn = sqlite3.connect(DATABASE_NAME)
        res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [name[0] for name in res]
        if not tables:
            flag = False
        else:
            for name in tables:
                if name not in NAME_TABLE:
                    flag = False
                    break
        conn.close()
        assert flag


    def test_type_column():
        """проверка имена и типов созданных столбцов в каждой таблицу"""

        global COLUMN_TYPE
        global DATABASE_NAME
        global NAME_TABLE
        conn = sqlite3.connect(DATABASE_NAME)
        flag = False
        for table in NAME_TABLE:
            res = conn.execute("PRAGMA table_info({})".format(table))
            for i, column in enumerate(res):
                flag = True
                description_column = list(column)
                # преобразование строк (команд) в верхний регистр:
                for i1, elem in enumerate(description_column):
                    if type(elem) == str:
                        description_column[i1] = description_column[i1].upper()

                correct_description_column = list(COLUMN_TYPE[table][i])
                # преобразование строк (команд) в верхний регистр:
                for i2, elem in enumerate(correct_description_column):
                    if type(elem) == str:
                        correct_description_column[i2] = correct_description_column[i2].upper()

                if description_column != correct_description_column:
                    flag = False
                    break
            if flag is False:
                break
        conn.close()
        assert flag

# тесты для lab1c
elif parameters['WORK'] == 'lab1c':
    pass

else:
    print('Такой {} лабораторной работы не существует'.format(parameters['WORK']))
