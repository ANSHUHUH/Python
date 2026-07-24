num = int(input("Enter number: "))
dig = 0
sum = 0
while num > 0 :
    dig = num %  10
    sum += dig
    num = num // 10
print("The sum of digits of ",num," is ",sum)
