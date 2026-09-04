people ={
    1:{"name":"Alin","age":"25","city":"New York"},
    2:{"name":"Bob","age":"30","city":"Los Angeles"},
    3:{"name":"Charlie","age":"28","city":"Chicago"}
}
for key in people:
    print("Person:",key)
    print("Name",people[key]["name"])
    print("Age",people[key]["age"])
    print("City:",people[key]["city"])
    print()