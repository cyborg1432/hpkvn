import mysql.connector


config = {
    "host":"localhost",
    "username":"root",
    "password":"toor",
    "port":"3307",
    "database":"contact_manager"
}


# Main Sub Execution

def add_contact():


    number = input("Enter New Number")
    name = input("Enter New Name")

    # Database Management
    conn = mysql.connector.connect(**config)

    if conn.is_connected():

        cursor = conn.cursor()
        add_query = f'insert into details(number,name) values("{str(number)}","{str(name)}")'
        cursor.execute(add_query)
        conn.commit()

        cursor.close()
        conn.close()

    else:
        print("not connected")


def show_specific_contact():
    number = input("Enter Contact Number to Search")

    conn = mysql.connector.connect(**config)

    if conn.is_connected():

        cursor = conn.cursor()
        cursor.execute(f"select * from details where number = {number}")
        result = cursor.fetchall()
        print(result)
        cursor.close()

    else:
        print("not connected")


def show_all_contact():
    # Database Management
    conn = mysql.connector.connect(**config)

    if conn.is_connected():

        cursor = conn.cursor()
        cursor.execute("select * from details")
        result = cursor.fetchall()
        for i in result:
            print(i)
        cursor.close()

    else:
        print("not connected")


def delete_specific_contact():
    number = input("Enter New Number")


    # Database Management
    conn = mysql.connector.connect(**config)

    if conn.is_connected():

        cursor = conn.cursor()
        delete_query = f'delete from details where number = {number}")'
        cursor.execute(delete_query)
        conn.commit()

        cursor.close()
        conn.close()

    else:
        print("not connected")







#Main Execution
while True:

    print("\t Welcome to the Contact Manager using MySQL")

    print('''Enter Your Preference
        1. Add Contact
        2. See Specific Contact
        3. See All Contacts
        4. Delete Specific Contact
    ''')

    uI = int(input("Enter Your Choice"))

    if(uI==1):
        add_contact()
    elif(uI==2):
        show_specific_contact()
    elif(uI==3):
        show_all_contact()
    elif(uI==4):
        delete_specific_contact()
    else:
        print("You Select Invalid Choice")