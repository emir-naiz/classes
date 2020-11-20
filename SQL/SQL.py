import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor() #cursor - для выполнение комманд на языке SQL

# cursor.execute("""CREATE TABLE Students(
#                 name varchar(50) NOT NULL ,
#                 last_name varchar(50),
#                 phone int )""")
# cursor.execute("INSERT INTO Students (name, last_name, phone) VALUES ('emir', 'naizabekov', '0704507705')")
# cursor.execute("INSERT INTO Students (name, last_name, phone) VALUES ('maksim', 'surovkin', '0123456789')")
# cursor.execute("INSERT INTO Students (name, last_name, phone) VALUES ('aijana', 'abd', '0123456789')")
# cursor.execute("INSERT INTO Students (name, last_name, phone) VALUES ('meerim', 'azarova', '0123456789')")
# cursor.execute("INSERT INTO Students (name, last_name, phone) VALUES ('baizak', 'madzhinov', '0123456789')")
# cursor.execute("INSERT INTO Students (name, last_name, phone) VALUES ('nazira', 'ken', '0123456789')")
# cursor.execute("INSERT INTO Students (name, last_name, phone) VALUES ('zarina', 's', '0123456789')")
# cursor.execute("SELECT * FROM Students")
# cursor.execute("ALTER TABLE Students ADD salary INT")
# cursor.execute("UPDATE Students SET salary = 1000000 WHERE name = 'meerim'")
# cursor.execute("SELECT name, salary FROM Students WHERE salary BETWEEN 100000 AND 1000000")
# cursor.execute("UPDATE Students SET phone = 0700216612 WHERE name = 'meerim' ")
# cursor.execute("DELETE FROM Students WHERE salary >= 1000000")
# cursor.execute("UPDATE Students SET sex = 1 WHERE name = 'zarina'")
print(cursor.fetchall())
connection.commit()

