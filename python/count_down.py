import time

user_input = int(input("Enter Numbers of Seconds for count Down"))


for i in range(1,user_input + 1):
    print(user_input - i +1)
    time.sleep(1)

