# dbmng

Для отправки и проверки работ dbmng

## Струтура

- requirements.txt \- все необходимые зависимости, чтобы все работало. Необходимо установить.
- main.py \- основной скрипт для работы
- variants \- дирректория, в которой содержится вспомогательные данные для тестирования для каждого варианта заданий.
- correct_works \- дирректория, в которой содержится правильные решенные задания для каждой работы и варианта.
- make\_test.py \- вспомогательная программа для написания тестов к работам
- test\_work.py \- написанные тесты для работ
- labworks.docx \- лабораторный практикум

## Как все работает?
Студент отправляет файл выполненной лаб. работы

Файл должен иметь строго определенное имя:
  <инициалы>\_<имя\_работы>\_<номер\_варианта>.<тип\_файла>
  
  Пример: gar\_lab1a\_0.txt
  
Файл для проверки должен находиться в корневой папке проекта.

Далее запускается скрипт main.py с параметрами из консоли

**python3 main.py <имя файла для проверки>** 

Пример: python3 main.py gar\_lab1a\_0.txt

Что делает скрипт main.py:
1.	Подготавливает рабочее пространство для проверки: удаляет БД если была
2.	Создает параметризованный файл parameters.txt, где содержится имя работы, инициалы, номер лабораторной, вариант и пр

Пример содержания parameters.txt:
- WORK\_FILE\_NAME=gar\_lab1a\_0.txt
- AUTHOR=gar
- WORK=lab1a
- VARIANT=0
- DATABASE_NAME='mydatabase.db'

После этого запускается тесты командой

  **pytest -q test_work.py**
  
В зависимости от работы и предосталвенного варианта система сама подберет нужный тест

Примечание: ключ -q это тихий режим, необязателен

test_work.py обращается к параметризованному файлу, чтобы найти правильные данные для проверки согласно варианту задания.
Все файлы для проверки варианты задания хранятся в variants/variants\_<имя\_лабораторной\_работы>/varinat\_<вариант>

Пример: variants/variants\_lab1a/variant\_0.py

variant\_0.py – простой файл, где хранятся правильные данные для првореки: какие должны быть имена таблиц, типы столбцов и прочее

--- 

## Списко лабораторный работ с вариантами

labworks.docx 

## Список доступных работ

- lab1a
- lab1b

## Как добавить вариант в систему

1. Необходимо письменно добавить задание в labworks.docx, где сформулировать четкие требования. 
2. Написать "правильную" работу к этому варианту. Сохранить его в файле correct\_<имя\_работы>\_<номер варианта>.<тип файла>
Пример: correct_lab1a_0.txt
4. Добавить файл в директорию correct_works в нужную папку
5. python3 make_test.py <имя_файла_файл>
Пример: python3 make_test.py correct_lab1a_0.txt
6. Все. Программа извлекла правильные данные к тесту (добавила в директорию variants) и файл больше не нужен.
