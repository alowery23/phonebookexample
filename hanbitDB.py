from distutils.util import execute
import pymysql

conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='@MNmn0065', db='hanbitdb', charset='utf8')
cur = conn.cursor()
sql = "CREATE TABLE IF NOT EXISTS userTable (ID char(7), USERNAME char(15), EMAIL char(20), BIRTHYEAR int)"
cur.execute(sql)
while(True):
    data1 = input("User ID ==>")
    if data1 == "":
        break
    data2 = input("User Name==>")
    data3 = input("User Email==>")
    data4 = input("User BirthYear==>")
    sql = "INSERT INTO userTable VALUES('"+data1 + \
        "','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)


conn.commit()
conn.close()
