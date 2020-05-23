# основной скрипт
# python3 main.py <скрипт.py/file.txt>
# пример запуска: python3 main.py gar_lab1a_0.txt

import sqlite3
import os
import sys

# имя файла с параметрами
NAME_PARAMETERS_FILE = 'parameters.txt'

# имя БД
DATABASE_NAME = 'mydatabase.db'

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

# elif len(sys.argv) == 3:
#
#     if not os.path.exists(sys.argv[1]):
#         print('файл не найден', sys.argv[1])
#         raise FileNotFoundError
#
#     else:
#         WORK_FILE_NAME = sys.argv[1]
#         author_work_variant = sys.argv[1].split('_')
#         AUTHOR = author_work_variant[0]
#         WORK = author_work_variant[1]
#         VARIANT = author_work_variant[2]
#         DATABASE_NAME = sys.argv[2]
#         if not DATABASE_NAME.endswith('.db'):
#             DATABASE_NAME = DATABASE_NAME + '.db'

else:
    print('error >3')
    raise AttributeError

# записываем параметры в файл NAME_PARAMETERS_FILE
parameters_file = open(NAME_PARAMETERS_FILE, 'w')
print('WORK_FILE_NAME=', WORK_FILE_NAME, file=parameters_file, sep='')
print('AUTHOR=', AUTHOR, file=parameters_file, sep='')
print('WORK=', WORK, file=parameters_file, sep='')
print('VARIANT=', VARIANT, file=parameters_file, sep='')
print('DATABASE_NAME=', DATABASE_NAME, file=parameters_file, sep='')
parameters_file.close()

# очищаем рабочую среду перед выполнением скрипта / запроса
if os.path.exists(DATABASE_NAME):
    os.remove(DATABASE_NAME)

# выполнение запроса / скрипта
if WORK_FILE_NAME.endswith('.txt'):
    """если это sql запрос в виде file.txt"""

    file = open(WORK_FILE_NAME, 'r')
    query = file.read()
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        conn.executescript(query)
        conn.commit()
        conn.close()
        print('ok')

    except:
        print('error')
        raise ValueError

elif WORK_FILE_NAME.endswith('.py'):
    """если это py скрипт"""

    print('это скрипт')

else:
    """это не скрипт и не запрос sql"""
    raise FileNotFoundError
