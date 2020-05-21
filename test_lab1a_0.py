import pytest
import sqlite3
import os
from execute_sql_query import DATABASE_NAME


def test_existDB():
    """существует ли БД"""

    flag = True
    if not os.path.exists(DATABASE_NAME):
        flag = False
    assert flag == True


def test_existNamedTable():
    """существует ли таблица с нужным именем"""

    NAME_TABLE = 'employees'
    conn = sqlite3.connect(DATABASE_NAME)
    res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [name[0] for name in res]
    name_table = tables[0]
    conn.close()
    assert NAME_TABLE == name_table


def test_column_names():
    """таблица содержит нужные столбцы в нужном порядке"""

    NAME_COLUMNS = ['id', 'name', 'birthday', 'sex', 'active', 'salary']
    conn = sqlite3.connect(DATABASE_NAME)
    res = conn.execute('select * from employees')
    name_columns = list(map(lambda x: x[0], res.description))
    conn.close()
    assert name_columns == NAME_COLUMNS


def test_type_column():
    """проверка имена столбцов и их типы (описание) """

    COLUMN_TYPE = [  # правильное описание столбцов
        # SQL: PRAGMA table_info(имя_таблицы)
        (0, 'id', 'INT UNSIGNED', 1, None, 0),
        (1, 'name', 'VARCHAR(20)', 1, None, 0),
        (2, 'birthday', 'DATETIME', 1, None, 0),
        (3, 'sex', 'VARCHAR(1)', 1, None, 0),
        (4, 'active', 'BOOL', 0, 'FALSE', 0),
        (5, 'salary', 'MEDIUMINT UNSIGNED', 1, None, 0),
    ]
    conn = sqlite3.connect(DATABASE_NAME)
    flag = True
    res = conn.execute('PRAGMA table_info(employees)')
    for i, column in enumerate(res):

        description_column = list(column)  # преобразование строк в верхний регистр
        for i1, elem in enumerate(description_column):
            if type(elem) == str:
                description_column[i1] = description_column[i1].upper()

        correct_description_column = list(COLUMN_TYPE[i])  # преобразование строк в верхний регистр
        for i2, elem in enumerate(correct_description_column):
            if type(elem) == str:
                correct_description_column[i2] = correct_description_column[i2].upper()

        if description_column != correct_description_column:
            flag = False
            break
    conn.close()
    assert flag == True
