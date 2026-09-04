my_d={
    "Apple":10,
    "kiwi":"yellow",
    "banana":15,
    "price":5.5,
    "note":"fruit"
}
total=0
for value in my_d.values():
    if isinstance(value,(int,float)):
        total+=value
print("The sum of all numaric values in dictionary is:",total)