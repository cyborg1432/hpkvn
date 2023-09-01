import json
import time


def add_contact():
    file = open("contact_manager.json", "r")
    dataArray = list(json.load(file))


    name = input("Enter User Name")
    user_number = input("Enter User Number")

    saving_template = {
        "name":name,
        "number":user_number
    }


    dataArray.append(saving_template)


    writeFile = open("contact_manager.json",'w')
    writeFile.write(json.dumps(dataArray))




def show_contact():
    file = open("contact_manager.json","r")
    dataArray = json.load(file)


    for i in range(0,len(dataArray)):
        print(dataArray[i]['number'] + "\t" + dataArray[i]['name'])

    file.close()










while 0==0:

    print('''Select your Choice
            1. Add Contact
            2. See Contact List
            3. Exit
    ''')

    req = int(input("Enter Your Choice"))

    if req == 1:
        #Add contacts
        add_contact()

    elif req == 2:
        #Show contacts
        show_contact()

    elif req == 3:
        exit(0)
    else:
        print("Invalid Choice Please Enter a valid choice")


    time.sleep(1)

    print("\n\n\n")
