from PyQt5.QtSql import QSqlDatabase
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("conctacts.sqlite")
con.open()
print(con.isOpen())