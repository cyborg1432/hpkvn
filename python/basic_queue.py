x = []

def enqueue(x):
    value = int(input("Enter Enqueue Value"))
    x.append(value)

def dequeue(x):
    x.remove(x[0])

def show():
    print(x)

while 0==0:
    print('''
        1. Enqueue
        2. Dequeue
        3. Show
        4. Exit
    ''')

    userInput = int(input("enter your choice"))

    if(userInput == 1):
        enqueue(x)
    elif(userInput == 2):
        dequeue(x)
    elif(userInput == 3):
        show()
    else:
        exit(0)