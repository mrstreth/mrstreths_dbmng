import sqlite3
import os
import sys

NAME_PARAMETERS_FILE = 'parameters.txt'

# python3 main.py <скрипт.py/file.txt> [<имя_бд>]
# python3 main.py gar_lab1a_0.txt
if len(sys.argv) < 2:
    print('error <2')
    raise AttributeError

elif len(sys.argv) == 2:

    if not os.path.exists(sys.argv[1]):
        print('файл не найден', sys.argv[1])
        raise FileNotFoundError
    else:
        WORK_FILE_NAME = sys.argv[1]
        author_work_variant = sys.argv[1].split('_')
        AUTHOR = author_work_variant[0]
        WORK = author_work_variant[1]
        VARIANT = author_work_variant[2].split('.')[0]
        DATABASE_NAME = 'mydatabase.db'

elif len(sys.argv) == 3:

    if not os.path.exists(sys.argv[1]):
        print('файл не найден', sys.argv[1])
        raise FileNotFoundError

    else:
        WORK_FILE_NAME = sys.argv[1]
        author_work_variant = sys.argv[1].split('_')
        AUTHOR = author_work_variant[0]
        WORK = author_work_variant[1]
        VARIANT = author_work_variant[2]
        DATABASE_NAME = sys.argv[2]
        if not DATABASE_NAME.endswith('.db'):
            DATABASE_NAME = DATABASE_NAME + '.db'

else:
    print('error >3')
    raise AttributeError

# если есть параметризованный файл - удаляем
# необходим для тестов
if os.path.exists(NAME_PARAMETERS_FILE):
    os.remove(NAME_PARAMETERS_FILE)
parameters_file = open(NAME_PARAMETERS_FILE, 'w')
print('WORK_FILE_NAME=', WORK_FILE_NAME, file=parameters_file, sep='')
print('AUTHOR=', AUTHOR, file=parameters_file, sep='')
print('WORK=', WORK, file=parameters_file, sep='')
print('VARIANT=', VARIANT, file=parameters_file, sep='')
print('DATABASE_NAME=', DATABASE_NAME, file=parameters_file, sep='')

# очищаем рабочую среду - удаляем бд
if os.path.exists(DATABASE_NAME):
    os.remove(DATABASE_NAME)

# проверка отправленного файла и дальнейшие с ним операции
if WORK_FILE_NAME.endswith('.txt'):
    """если это sql запрос в виде txt file"""

    from execute_sql_query import execute_query

    file = open(WORK_FILE_NAME, 'r')
    query = file.read()
    try:
        execute_query(query, DATABASE_NAME)
        print('ok')
    except:
        print('error')
        raise ValueError

elif WORK_FILE_NAME.endswith('.py'):
    """если это py скрипт"""

    print('это скрипт')

else:
    print('error >3')
    raise AttributeError

#-----------------------------------------------------------------------
# DATABASE_NAME = 'mydatabase.db'
# # имя(имена) таблиц
# NAME_TABLE = ['employees']
#
# # типы столбцов
# COLUMN_TYPE = {  # правильное описание столбцов
#         # SQL: PRAGMA table_info(имя_таблицы)
#         'employees':
#                 [(0, 'id', 'INT UNSIGNED', 1, None, 0),
#                 (1, 'name', 'VARCHAR(20)', 1, None, 0),
#                 (2, 'birthday', 'DATETIME', 1, None, 0),
#                 (3, 'sex', 'VARCHAR(1)', 1, None, 0),
#                 (4, 'active', 'BOOL', 0, 'FALSE', 0),
#                 (5, 'salary', 'MEDIUMINT UNSIGNED', 1, None, 0)],
# }
# conn = sqlite3.connect(DATABASE_NAME)
# flag = True
# for table in NAME_TABLE:
#     res = conn.execute("PRAGMA table_info({})".format(table))
#     for i, column in enumerate(res):
#
#         description_column = list(column)
#         # преобразование строк (команд) в верхний регистр:
#         for i1, elem in enumerate(description_column):
#             if type(elem) == str:
#                 description_column[i1] = description_column[i1].upper()
#
#         correct_description_column = list(COLUMN_TYPE[table][i])
#         print(correct_description_column)
#         print(description_column)
#         # преобразование строк (команд) в верхний регистр:
#         for i2, elem in enumerate(correct_description_column):
#             if type(elem) == str:
#                 correct_description_column[i2] = correct_description_column[i2].upper()
#         print(correct_description_column)
#         print(description_column)
#         if description_column != correct_description_column:
#             flag = False
#             break
#     if flag is False:
#         break
# print(flag)