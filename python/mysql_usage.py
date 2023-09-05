import mysql.connector

config = {
    'user':'root',
    'password':'toor',
    'host':'localhost',
    'database':'joints'

}


# conn = mysql.connector.connect(user="root",password="toor",host="localhost",database="joints")

conn = mysql.connector.connect(**config)

if conn.is_connected():
    print("connected")
else:
    print("not connect")