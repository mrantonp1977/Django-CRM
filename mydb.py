import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Antonp@1977'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE antonp")

print("all done!")
