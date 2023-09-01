# def check(x):
#     if (int(x) == 5):
#         return "true"
#     else:
#         return "false"
#
#
# for i in range(1,4):
#     userInput = input("Enter Gussed Number")
#     if(check(userInput) == "true"):
#         print("You guess the right number")
#         break
#     else:
#         print("try Again")



def check(x):
    savedNumber = 5
    if(x == savedNumber):
        return "true"
    else:
        return "false"



for i in range(1,4):
    userInput = int(input("Enter Gussed Number"))
    if(check(userInput)== "true"):
        print("Success")
        break
    else:
        print("try again")



















