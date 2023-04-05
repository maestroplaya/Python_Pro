import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery


con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("animals.sqlite")

if not con.open():
    print(f"Database Error: {con.lastError().databaseText()}")
    sys.exit()

createTableQuery = QSqlQuery()
createTableQuery.exec(
    """
    CREATE TABLE animals (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40),
        type VARCHAR(50) NOT NULL
    )
    """
)

print(con.tables())