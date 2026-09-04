def print_String(s):
    if s=="":
        return
    print(s[0],end="")
    print_String(s[1:])
user_input=input("Enter a String:")
print("String printed using recurion:")
print_String(user_input)        