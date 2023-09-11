import random


def read_files():
    file = open("09-09-2023-test.txt", 'r')
    print(file.read())
    file.close()


def write_files():
    file = open("09-09-2023-test.txt", 'a')
    content = input("Enter File Content")
    file.write(content)
    file.close()


def print_numbers():
    my_range = int(input("Enter Your Number range"))
    for i in range(0, my_range + 1):
        print(i)


def json_usage():
    x = {"name":"Deepanshu","class":"hpkvn","age":"32"}
    print(f"The name is {x['name']}, the class is {x['class']} and the age is {x['age']}")


def random_joke():
    jokes = ['Joke 1','Joke 2','Joke 3']
    print(random.choice(jokes))


while True:
    print("\t Practical Saturday 09-09-2023")
    print('''Choose your Choice
        1. Read Files
        2. Write Files (Append)
        3. Print No's with range
        4. Dictionary/JSON Usage
        5. Random Joke
    ''')
    x = int(input("Enter Your Choice"))

    if x == 1:
        read_files()
    elif x == 2:
        write_files()
    elif x == 3:
        print_numbers()
    elif x == 4:
        json_usage()
    elif x == 5:
        random_joke()
    else:
        print("You are providing Invalid Choice")
        exit(0)
