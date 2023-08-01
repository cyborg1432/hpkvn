num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))

print("Select Serial Number to Appling operation name : ")
print('''
1. Addition \n 
2. Substraction \n 
3. Multiplication \n 
4. Division \n 
5. Floor Division \n
6. Modulus (Remainder) \n''')

op = int(input("Enter Opearation Name : "))

if(op == 1):
    print(f"the Addition of two number {num1} and {num2} is : " , num1 + num2)
elif(op ==2):
    print(f"the Substraction of two number {num1} and {num2} is : " , num1 - num2)
elif(op ==3):
    print(f"the Multiplication of two number {num1} and {num2} is : " , num1 * num2)
elif(op ==4):
    print(f"the Division of two number {num1} and {num2} is : " , num1 / num2)
elif(op ==5):
    print(f"the Floor Division of two number {num1} and {num2} is : " , num1 // num2)
elif(op ==6):
    print(f"the Modulus of two number {num1} and {num2} is : " , num1 % num2)
else:
    print("invalid operation choose")