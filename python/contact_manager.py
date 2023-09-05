# import json
# import time
#
#
# def add_contact():
#     file = open("contact_manager.json", "r")
#     dataArray = list(json.load(file))
#
#
#     name = input("Enter User Name")
#     user_number = input("Enter User Number")
#
#     saving_template = {
#         "name":name,
#         "number":user_number
#     }
#
#
#     dataArray.append(saving_template)
#
#
#     writeFile = open("contact_manager.json",'w')
#     writeFile.write(json.dumps(dataArray))
#
#
#
#
# def show_contact():
#     file = open("contact_manager.json","r")
#     dataArray = json.load(file)
#
#
#     for i in range(0,len(dataArray)):
#         print(dataArray[i]['number'] + "\t" + dataArray[i]['name'])
#
#     file.close()
#
#
# def search_by_contact(x):
#     file = open("contact_manager.json","r")
#     dataArray = json.load(file)
#
#     result = 0
#
#     for i in range(0,len(dataArray)):
#         if dataArray[i]['number'] == x:
#             result = dataArray[i]['number'] + "\t" + dataArray[i]['name']
#             break
#         else:
#             result = "This number don't exists"
#
#
#     print(result)
#
#     file.close()
#
#
#
# while 0==0:
#
#     print('''Select your Choice
#             1. Add Contact
#             2. See Contact List
#             3. Search by Contact
#             4. Exit
#     ''')
#
#     req = int(input("Enter Your Choice"))
#
#     if req == 1:
#         #Add contacts
#         add_contact()
#
#     elif req == 2:
#         #Show contacts
#         show_contact()
#
#     elif req == 3:
#         #Search By contact
#         x = str(input("Enter User Contact Number to Search"))
#         search_by_contact(x)
#
#     elif req == 4:
#         exit(0)
#     else:
#         print("Invalid Choice Please Enter a valid choice")
#
#
#     time.sleep(1)
#
#     print("\n\n\n")


import json




def write(name, contact):
    with open('vishi.json', 'r') as file:
        data = json.load(file)
        students = data.get('students', [])

        students.append({"name": name, "phone": contact})

    with open('vishi.json', 'w') as file:
        data['students'] = students
        json.dump(data, file)


def show():
    with open('vishi.json', 'r') as file:
        data = json.load(file)
        students = data.get('students', [])
        if students:
            for student in students:
                print(f"My name is {student['name']} and contact no is {student['phone']}")
        else:
            print("No contacts found.")





choice = int(input('''Choose 1. Add contact \n2. Show contacts \n3. Exit\nEnter your choice: '''))

if choice == 1:
    name = input("Enter your Name: ")
    contact = input("Enter Your number: ")
    write(name, contact)
    print("Contact added successfully.")
elif choice == 2:
    show()
elif choice == 3:
    print("Exit")
else:
    print("Invalid choice")

