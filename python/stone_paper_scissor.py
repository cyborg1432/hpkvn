import random

value_array = ['Stone','Paper','Scissor']

computer_selection = random.randint(0,4) - 1

print('''Enter Number to choose your choice \n
        1. Stone \n
        2. Paper \n
        3. Scissor \n
''')

user_input = int(input("Enter Your Selection")) -1



if(computer_selection == user_input):
    print(f"Draw Because the user selection is {value_array[user_input]} and Computer Selection is {value_array[computer_selection]} ")
elif(value_array[user_input]=="Stone" and value_array[computer_selection] == "Scissor"):
    print(f"Win becuase user input is {value_array[user_input]} and computer input is {value_array[computer_selection]}")
elif(value_array[user_input]=="Stone" and value_array[computer_selection] == "Paper"):
    print(f"You Lose because user input is {value_array[user_input]} and computer selection is {value_array[computer_selection]}")
elif(value_array[user_input]=="Paper" and value_array[computer_selection] == "Scissor"):
    print(f"You Loose because user select {value_array[user_input]} and computer selection is {value_array[computer_selection]}")
elif(value_array[user_input]=="Paper" and value_array[computer_selection]=="Stone"):
    print(f"Win becuase user input is {value_array[user_input]} and computer input is {value_array[computer_selection]}")
elif(value_array[user_input]=="Scissor" and value_array[computer_selection]=="Stone"):
    print(f"You Loose because user select {value_array[user_input]} and computer selection is {value_array[computer_selection]}")
elif(value_array[user_input]=="Scissor" and value_array[computer_selection]=="Paper"):
    print(f"Win becuase user input is {value_array[user_input]} and computer input is {value_array[computer_selection]}")


