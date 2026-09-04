student={
    "student_1":{"name":"alic","age":"25","city":"Landan"},
    "student_2":{"name":"piyush","age":"20","city":"Mumbai"},
    "student_3":{"name":"Rishi","age":"20","city":"Sion"}
}
print("All keys and values in the nested dictionery:\n")
for student_key,student_info in student.items():
    print(f"{student_key}:")
    for key,value in student_info.items():
        print(f"{key}:{value}")
    print()    