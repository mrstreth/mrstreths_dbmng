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
    """содержит ли таблица нужные поля"""
    COLUMN_TYPE = [
        (0, 'id', 'INT unsigned', 1, None, 0),
        (1, 'name', 'varchar(20)', 1, None, 0),
        (2, 'birthday', 'DATETIME', 1, None, 0),
        (3, 'sex', 'varchar(1)', 1, None, 0),
        (4, 'active', 'BOOL', 0, 'FALSE', 0),
        (5, 'salary', 'mediumint unsigned', 1, None, 0),
    ]
    # не доделал
    assert True
