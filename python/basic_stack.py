def perform_push(x):
    value = input("Enter the number to Push")
    x.append(value)

def perform_pop(x):
    x.remove(x[len(x)-1])

def show_stack(x):
    print(x)


x=[]

while 0==0:
    print('''
        1. Push
        2. Pop
        3. See Stack
        4. Exit
    ''')

    userInput = int(input("enter your choice"))

    if(userInput == 1):
        perform_push(x)

    elif(userInput == 2):
        perform_pop(x)
    elif(userInput == 3):
        show_stack(x)
    else:
        exit(0)