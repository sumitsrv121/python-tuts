from mysql.connector import connect

mydb = connect(host="localhost", user="", passwd="")

cursor = mydb.cursor()

# cursor.execute("SHOW DATABASES")
#
# rows = cursor.fetchall()
#
# # for row in rows:
# #     print(row)
# cursor.execute("select * from telusko.student")
# fetchall = cursor.fetchall()
# for row in fetchall:
#     print(row)


cursor.execute("INSERT INTO telusko.student value(%s,%s)", ("sumit", "Heritage"))

mydb.commit()

cursor.execute("select * from telusko.student")
fetchall = cursor.fetchall()
for row in fetchall:
    print(row)

cursor.close()
mydb.close()
