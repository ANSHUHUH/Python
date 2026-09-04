with open("demo2.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
for i in range(0,len(lines),2):
    print(lines[i].strip())