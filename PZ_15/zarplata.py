import sqlite3 as sq
from anketa import anketa_info
from boln_lists import boln_lists_info



with sq.connect('zarplata.db') as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS anketa (
         anketa_id INTEGER PRIMARY KEY,
         name VARCHAR(50),
         surname VARCHAR(50),
         birthday DATE,
         pol VARCHAR(15),
         data_naima DATE,
         dolzhnost VARCHAR(50),
         otdel VARCHAR(50),
         bazovaia_stavka DECIMAL(8, 1)
     )""")
    cur.execute("DELETE FROM anketa")


with sq.connect('zarplata.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO anketa VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", anketa_info)



with sq.connect('zarplata.db') as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS boln_lists (
         boln_lists_id INTEGER PRIMARY KEY,
         anketa_id INTEGER,
         data_start DATE,
         data_end DATE,
         prichina VARCHAR(500),
         diagnoz VARCHAR(500),
         oplachen BOOLEAN,
         FOREIGN KEY (anketa_id) REFERENCES anketa (anketa_id)
     )""")
    cur.execute("DELETE FROM boln_lists")


with sq.connect('zarplata.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO boln_lists VALUES (?, ?, ?, ?, ?, ?, ?)", boln_lists_info)




with sq.connect('zarplata.db') as con:
    cur = con.cursor()

    #SQL-запросы на выборку данных


    # 1 Вывести список всех сотрудников и их должностей
    print(*cur.execute("SELECT name, surname, dolzhnost FROM anketa").fetchall())
    
    # 2 Вывести список всех сотрудников и их базовых ставок
    print(*cur.execute("SELECT name, surname, bazovaia_stavka FROM anketa").fetchall())
    
    # 3 Вывести список всех сотрудников, работающих в отделе IT
    print(*cur.execute("SELECT name, surname FROM anketa WHERE otdel == 'Отдел IT'").fetchall())
    
    # 4 Вывести список всех сотрудников, принятых на работу после 1 января 2022 года
    print(*cur.execute("SELECT name, surname FROM anketa WHERE data_naima > '2022-01-01'").fetchall())
    
    # 5 Вывести список всех боьничных листов, выписанных сотруднику с id = 42
    print(*cur.execute("SELECT boln_lists_id FROM boln_lists WHERE anketa_id == 42").fetchall())
    
    # 6 Вывести список всех больничных листов, оплаченных компанией
    print(*cur.execute("SELECT boln_lists_id FROM boln_lists WHERE oplachen == 1").fetchall())

    # 7 Вывести список всех сотрудников, имеющих больничные листы за текущий месяц
    print(*cur.execute("SELECT name, surname FROM anketa INNER JOIN boln_lists ON boln_lists.anketa_id = anketa.anketa_id WHERE data_end BETWEEN '2023-04-01' AND '2023-04-30'").fetchall())

    # 8 Вывести среднюю базовую ставку всех сотрудников
    print(*cur.execute("SELECT AVG(bazovaia_stavka) FROM anketa").fetchall())

    # 9 Вывести список всех сотрудников, имеющих базовую ставку выше 100 000
    print(*cur.execute("SELECT name, surname FROM anketa WHERE bazovaia_stavka > 100000").fetchall())

    # 10  Вывести список всех сотрудников и общее количество дней, проведенных ими на больничном
    print(*cur.execute("SELECT name, surname, JULIANDAY(data_end) - JULIANDAY(data_start) FROM anketa INNER JOIN boln_lists ON boln_lists.anketa_id = anketa.anketa_id").fetchall())

    # 11 Вывести информацию о сотрудниках и их больничных листах за последний месяц
    print(*cur.execute("SELECT name, surname, boln_lists_id, prichina, diagnoz FROM anketa INNER JOIN boln_lists ON boln_lists.anketa_id = anketa.anketa_id WHERE data_end BETWEEN '2023-04-01' AND '2023-04-30'").fetchall())

    # 12 Вывести среднюю продолжительность больничных листов сотрудников в каждом отделе
    print(*cur.execute("SELECT JULIANDAY(data_end) - JULIANDAY(data_start) FROM boln_lists INNER JOIN anketa ON boln_lists.anketa_id = anketa.anketa_id WHERE otdel = 'Отдел IT'").fetchall())
    print(*cur.execute("SELECT JULIANDAY(data_end) - JULIANDAY(data_start) FROM boln_lists INNER JOIN anketa ON boln_lists.anketa_id = anketa.anketa_id WHERE otdel = 'Отдел бухгалтерии'").fetchall())
    print(*cur.execute("SELECT JULIANDAY(data_end) - JULIANDAY(data_start) FROM boln_lists INNER JOIN anketa ON boln_lists.anketa_id = anketa.anketa_id WHERE otdel = 'Отдел менеджмента'").fetchall())
    print(*cur.execute("SELECT JULIANDAY(data_end) - JULIANDAY(data_start) FROM boln_lists INNER JOIN anketa ON boln_lists.anketa_id = anketa.anketa_id WHERE otdel = 'Отдел продаж'").fetchall())

    # 13 Вывести список сотрудников и информацию о последнем больничном листе, который они оформляли
    print(*cur.execute("SELECT name, surname, boln_lists_id, prichina, diagnoz, data_start, data_end FROM anketa INNER JOIN boln_lists ON boln_lists.anketa_id = anketa.anketa_id WHERE (boln_lists.anketa_id, boln_lists.data_end) IN (SELECT anketa_id, MAX(data_end) FROM boln_lists GROUP BY anketa_id)").fetchall())

    # 14 Вывести список сотрудников и информацию о первом больничном листе, который они оформляли
    print(*cur.execute("SELECT name, surname, boln_lists_id, prichina, diagnoz, data_start, data_end FROM anketa INNER JOIN boln_lists ON boln_lists.anketa_id = anketa.anketa_id WHERE (boln_lists.anketa_id, boln_lists.data_start) IN (SELECT anketa_id, MIN(data_start) FROM boln_lists GROUP BY anketa_id)").fetchall())

    # 15 Вывести список сотрудников и суммарную продолжительность их больничных листов в текущем году
    print(*cur.execute("SELECT name, surname, JULIANDAY(data_end) - JULIANDAY(data_start) FROM boln_lists INNER JOIN anketa ON boln_lists.anketa_id = anketa.anketa_id WHERE data_end BETWEEN '2023-01-01' AND '2023-12-31'").fetchall())



with sq.connect('zarplata.db') as con:
    cur = con.cursor()

    #SQL-запросы на обновление данных из БД


    # 1 Обновить базовую ставку сотрудника на определенной должности
    print(*cur.execute("UPDATE anketa SET bazovaia_stavka = bazovaia_stavka+25000 WHERE dolzhnost='Разработчик баз данных'").fetchall())

    # 2 Обновить отдел для всех сотрудников в определенном диапазоне возраста
    print(*cur.execute("UPDATE anketa SET otdel='Отдел менеджмента' WHERE birthday BETWEEN '2000-01-01' AND '2001-01-01'").fetchall())

    # 3 Обновить дату найма для сотрудника, получившего повышение
    print(*cur.execute("UPDATE anketa SET data_naima='2022-02-02' WHERE dolzhnost='Разработчик баз данных'").fetchall())

    # 4 Обновить причину больничного листа для сотрудника
    print(*cur.execute("UPDATE boln_lists SET prichina='Боль в горле и кашель' WHERE anketa_id=100").fetchall())



with sq.connect('zarplata.db') as con:
    cur = con.cursor()

    #SQL-запросы удаление данных из БД


    # 1 Удалить все записи о больничных листах для сотрудника с именем "Иван"
    # print(*cur.execute("DELETE FROM boln_lists WHERE anketa_id IN (SELECT anketa_id FROM anketa WHERE name='Иван')").fetchall())

    # 2 Удалить все записи о больничных листах для сотрудника с фамилией "Петров"
    # print(*cur.execute("DELETE FROM boln_lists WHERE anketa_id IN (SELECT anketa_id FROM anketa WHERE surname='Петров')").fetchall())

    # 3 Удалить все записи о больничных листах для сотрудника с должностью "Менеджер"
    # print(*cur.execute("DELETE FROM boln_lists WHERE anketa_id IN (SELECT anketa_id FROM anketa WHERE dolzhnost='Менеджер')").fetchall())

    # 4 Удалить все записи о больничных листах для сотрудника с отделом "Отдел продаж"
    # print(*cur.execute("DELETE FROM boln_lists WHERE anketa_id IN (SELECT anketa_id FROM anketa WHERE otdel='Отдел продаж')").fetchall())

    # 5 Удалить все записи о больничных листах для сотрудника женского пола
    # print(*cur.execute("DELETE FROM boln_lists WHERE anketa_id IN (SELECT anketa_id FROM anketa WHERE pol='Женский')").fetchall())

    # 6 Удалить все записи о больничных листах для сотрудников старше 50 лет
    # print(*cur.execute("DELETE FROM boln_lists WHERE anketa_id IN (SELECT anketa_id FROM anketa WHERE birthday > '1970-01-01')").fetchall())

    # 7 Удалить все записи о неоплаченных больничных листах
    # print(*cur.execute("DELETE FROM boln_lists WHERE oplachen = False").fetchall())

    # 8 Удалить все записи о больничных листах, дата окончания которых прошла
    # print(*cur.execute("DELETE FROM boln_lists WHERE data_end < '2023-04-20'").fetchall())

    # 9 Удалить все записи о больничных листах, начиная с определенной даты
    # print(*cur.execute("DELETE FROM boln_lists WHERE data_start > '2020-06-05'").fetchall())

    # 10 Удалить все записи о больничных листах, закончившихся до определенной даты
    # print(*cur.execute("DELETE FROM boln_lists WHERE data_end < '2020-06-05'").fetchall())

    # 11 Удалить все больничные листы сотрудника с именем "Иван" из таблицы "Больничные листы
    # print(*cur.execute("DELETE FROM boln_lists WHERE anketa_id IN (SELECT anketa_id FROM anketa WHERE name='Иван')").fetchall())

    # 12 Удалить все больничные листы сотрудников, чьи фамилии начинаются на букву "С" из таблицы "Больничные листы"
    # print(*cur.execute("DELETE FROM boln_lists WHERE anketa_id IN (SELECT anketa_id FROM anketa WHERE surname LIKE 'С%')").fetchall())

    # 13 Удалить все больничные листы, которые еще не были оплачены, у сотрудников с должностью "Менеджер" из таблицы "Больничные листы"
    # print(*cur.execute("DELETE FROM boln_lists WHERE oplachen = False AND anketa_id IN (SELECT anketa_id FROM anketa WHERE dolzhnost='Менеджер')").fetchall())

    # 14 Удалить все больничные листы, выписанные сотрудникам отдела "IT" в период с 1 января
    # print(*cur.execute("DELETE FROM boln_lists WHERE data_start > '2023-01-01' AND anketa_id IN (SELECT anketa_id FROM anketa WHERE otdel='Отдел IT')").fetchall())

    # 15 Удалить все больничные листы, связанные со сотрудниками старше 50 лет из таблицы "Больничные листы"
    # print(*cur.execute("DELETE FROM boln_lists WHERE anketa_id IN (SELECT anketa_id FROM anketa WHERE birthday > '1970-01-01')").fetchall())

