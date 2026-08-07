user_input=input("Enter a string:")
upper_count =0
lower_count =0

for char in user_input:
    if char.isupper():
        upper_count +=1
    elif char.islower():
            lower_count +=1

print("Numbers of Upper Case letters:" ,upper_count)
print("Numbers of Lower Case letters:" ,lower_count) 
