from distutils.util import execute
import pymysql

conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = None

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='@MNmn0065', db='hanbitdb', charset='utf8')
cur = conn.cursor()
cur.execute("SELECT * FROM userTable")

print("USER ID   USER NAME   EMAIL   BIRTHYEAR")
print("----------------------------------------")

while(True):
    row = cur.fetchone()
    if row == None:
        break
    data1, data2, data3, data4 = row

    print("%5s %15s %15s %d" % (data1, data2, data3, data4))


conn.close()
