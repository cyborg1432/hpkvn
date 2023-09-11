import mysql.connector
apart = {
    'username': 'root',
    'password': 'toor',
    'host': 'localhost',
    'database': 'vishi',
    'port':'3307'
    }

conn = mysql.connector.connect(**apart)
mycursor = conn.cursor()
if conn.is_connected():
    print("connected")
else:
    print("not connected")

def ins(name,phone):
    try:
        insert_que = "INSERT INTO contact (name,phone) VALUES (%s,%s)"
        mycursor.execute(insert_que,(name,phone))
        conn.commit()
        print("contact added ")
    except Exception as e:
        print("not added",str(e))
def show():
    try:
        mycursor.execute("SELECT * FROM contact;")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    except Exception as e:
        print(str(e))
def desk():
    try:
        user = input("enter the number to search:")
        search = ("SELECT name,phone FROM contact where name = %s OR phone = %s")
        mycursor.execute(search,(user,user))
        result = mycursor.fetchall()
        for x in result:
            print(f" name is {x[0]} and phone number is {x[1]}")
    except Exception as e:
        print(str(e))
def deli():
    try:
        user = input("enter the number to delete:")
        delete = ("DELETE FROM contact where name = %s OR phone = %s")
        mycursor.execute(delete,(user,user))
        result = mycursor.fetchall()
        if mycursor.rowcount > 0:
            print("deleted")
        else:
            print("error in deletion")
    except Exception as e:
        print(str(e))
while True:
    print("welcome to contact manager")
    print("1. add contact")
    print("2. show contact")
    print("3. search contact")
    print("4. delete contact")
    choice = int(input("enter your choice:"))
    if choice == 1:
        name = input("enter your name")
        phone = input("enter your number")
        ins(name,phone)
    elif choice == 2:
        show()
    elif choice == 3:
        desk()
    elif choice == 4:
        deli()
    else:
       print("error")
conn.close()