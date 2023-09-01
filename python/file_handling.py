# file = open('file_handling.txt','r')
#
# print(file.read())
#
# file.close()


# file = open("file_handling.txt",'w')
#
# file.write("Hello World")
#
# file.close()

#
# file = open('file_handling.txt','a')
#
# file.write("New Hello World")
#
# file.close()

# import json
#
# file = open('file_handling.json','r')
#
# x = json.load(file)
#
# print(x['data'][1])

import json

file = open("file_handling.json",'r')

x = json.load(file)

print(f"My Name is {x['name']}, and class is {x['class']} and roll no is {x['rollno']} ")

