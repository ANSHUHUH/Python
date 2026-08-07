numbers= input("Enter numbers separated by spaces:")

number_list =[int(num) for num in numbers.split()]

target = int(input("Enter the numbers to find:"))

count=0
for num in number_list:
    if num==target:
        count+=1

print(f"The number{target} occurs {count} time(s) in the list.")        
