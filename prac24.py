with open("demo.txt","r",encoding ="utf-8") as file1:
    content = file1.read()
with open("myfile.txt","a",encoding="utf-8") as file2:
    file2.write(content)
    print("contents of demo.txt have been added to myfile.txt")