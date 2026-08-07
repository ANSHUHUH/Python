fruits = ["apple" , "banana" , "cherry"]
print("Initial list", fruits)

fruits.append("orange")
print("After appending the orange:",fruits)

fruits.append("grape")
print("After appending the grape:",fruits)

fruits.remove("banana")
print("After removing the banana",fruits)

item_to_remove="kiwi"

if item_to_remove in fruits:

 fruits.remove(item_to_remove)
 print(f"After removing'{item_to_remove}' :", fruits)

else:
    print(f"{item_to_remove}' not found in the list.Nothing removed.")

print("Final list:" , fruits)
