import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("contacts.sqlite")

if not con.open():
    print(f"Database Error: {con.lastError().databaseText()}")
    sys.exit(1)

task_zero = """SELECT * FROM jobs"""
task_one = """SELECT * FROM users"""
task_two = """SELECT * FROM users 
                WHERE email IS NOT NULL;"""
task_three = """SELECT name FROM users 
                WHERE id != 1;"""
task_four = """SELECT name, salary FROM users 
                WHERE salary BETWEEN 5000 AND 10000;"""
task_five = """"""
task_six = """"""
task_seven = """SELECT COUNT(name) FROM users;"""
task_eight = """SELECT AVG(salary) AS avg_salary FROM users;"""
task_nine = """SELECT name, MAX(salary) FROM users WHERE job_id = 2;"""
task_ten = """SELECT job_id, COUNT(name) as count 
                FROM users GROUP BY job_id;"""
task_eleven = """SELECT job_id, AVG(salary) as avg_salary
                    FROM users
                    GROUP BY job_id
                    HAVING avg_salary > 20000"""
task_twelve = """SELECT name, salary FROM users ORDER BY salary DESC"""
task_thirteen = """SELECT name, job_id FROM users ORDER BY job_id, name"""
task_fourteen = """"""
task_fifteen = """INSERT INTO users (name, job_id) VALUES('Ligma Balls', 1);"""
task_sixteen = """INSERT INTO jobs (id, name) VALUES(6, 'Robot Mann');"""
task_seventeen = """UPDATE users SET job_id = 6 WHERE name='Ligma Balls';"""
query = QSqlQuery()
query.exec(task_zero)

count = query.record().count()
for i in range(count):
    print(query.record().fieldName(i), end='\t')
print()
while query.next():
    for i in range(count):
        print(query.value(i), end='\t')
    print()
