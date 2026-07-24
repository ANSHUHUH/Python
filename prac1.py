user_input = input("enter a string : ")
reversed_string =" "
index = len(user_input) -1
while index >= 0:
    reversed_string = reversed_string +user_input[index]
    index = index - 1

print("reversed stirng is : ",reversed_string)