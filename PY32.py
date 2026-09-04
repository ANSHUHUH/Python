items=["apple",123,"banana",45,"grap",8.8,"melon"]
string_count=0
for item in items:
    if type(item)== str:
        string_count=string_count+1
print("Number of String in list:",string_count)