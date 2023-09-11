import mysql.connector

config = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'testdb'

}


# conn = mysql.connector.connect(user="root",password="toor",host="localhost",database="joints")

conn = mysql.connector.connect(**config)




if conn.is_connected():

    cursor = conn.cursor()
    cursor.execute("select * from customers")
    result = cursor.fetchall()
    for i in result:
        print(i[0])


else:
    print("not connect")