# from sqlite3 import Cursor
import mysql.connector as mysql


def dbscript(sql,values):
    mydb=mysql.Connect(host='loclahost',user='root', database='pms',password='')
    cursor=mydb.cursor()
    cursor.execute(sql,values)
    mydb.commit()
    mydb.close()
    





















































































































































































































































































































































































































































































