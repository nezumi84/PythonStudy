import cx_Oracle

dsnStr = cx_Oracle.makedsn('127.0.0.1',1521,"orcl")
con = cx_Oracle.connect("hr","hr",dsnStr)
cursor = con.cursor()

cursor.execute('SELECT * FROM EMPLOYEES')
res = cursor.fetchall()

for row in res:
    value = str(row[0]) + " " + row[1] + " " + row[2]
    print(value)
cursor.close()
con.close()