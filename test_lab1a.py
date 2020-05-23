import pytest
import sqlite3
import os

NAME_PARAMETERS_FILE = 'parameters.txt'

parameters_file = open(NAME_PARAMETERS_FILE, 'r')
parameters = dict([line.strip().split('=') for line in parameters_file.readlines()])

command_import_test = \
    'from variants.variants_{WORK}.variant_{VARIANT} import DATABASE_NAME, NAME_TABLE, COLUMN_TYPE'.format(\
        WORK=parameters['WORK'], VARIANT=parameters['VARIANT'])
exec(command_import_test)


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
    name_table = tables
    for name in name_table:
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
    flag = True
    for table in NAME_TABLE:
        res = conn.execute("PRAGMA table_info({})".format(table))
        for i, column in enumerate(res):

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
