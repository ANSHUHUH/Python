try:
    with open("demo3.txt","r",encoding="utf-8") as file:
        lines= file.readlines()
        for i in range(min(5,len(lines))):
            print(lines[i],end="")
except FileNotFoundError:
    print("error - the file was not founded")
except PermissionError:
    print("error - permission not allowed")
except Exception as e:
    print("an expected error occured")