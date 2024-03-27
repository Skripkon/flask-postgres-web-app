import os
import psycopg2

# Установка соединения с БД
conn = psycopg2.connect(host="localhost",
                        database=os.environ['POSTGRES_DB'],
                        user=os.environ['USERNAME_DB'],
                        password=os.environ['PASSWORD_DB'])

# Курсор - это объект, позволяющий взаимодействовать с БД
cur = conn.cursor()

# Создание таблицы
cur.execute('DROP TABLE IF EXISTS Jokes;')
cur.execute('CREATE TABLE Jokes (id serial PRIMARY KEY,'
            'title varchar (150) NOT NULL,'
            'author varchar (50) NOT NULL,'
            'jokeText text,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);'
            )

# Вставка строки

cur.execute('INSERT INTO Jokes (title, author, jokeText)'
            'VALUES (%s, %s, %s)',
            ('О числах Фибоначчи',
             'Студент ПМИ',
             'Эта шутка про числа Фибоначчи даже хуже, чем предыдущие две вместе взятые')
            )

# Вставка строки

cur.execute('INSERT INTO Jokes (title, author, jokeText)'
            'VALUES (%s, %s, %s)',
            ('Физики шутят',
             'Неизвестный',
             'Не можете найти работу? Умножьте время на мощность!')
            )

# Сохранение операции
conn.commit()

# Закрытие соединения
cur.close()
conn.close()
