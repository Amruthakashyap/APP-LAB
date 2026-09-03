#search a student in a file
roll_search=input("enter roll number to search")
with open("student.txt", "r") as file:
    for line in file:
        roll,name,course,marks = line.strip().split(",")
        if roll==roll_search:
            print("Roll No:", roll )
            print("Name:", name)
            print("Course:", course)
            print("Marks:", marks)
            break
    else:
        print("Student not found")   

#copy one file to another                             
with open("student.txt", "r") as source:
    content=source.read()
with open("student_records.txt", "w") as destination:
    destination.write(content)
print("Backup created successfully")  


#donot overwrite in a file 
roll_search=input("enter roll number to search")
with open("student.txt", "a") as file:
    for line in file:
        roll,name,course,marks = line.strip().split(",")
        if roll==roll_search:
            print("Roll No:", roll )
            print("Name:", name)
            print("Course:", course)
            print("Marks:", marks)
            break
    else:
        print("Student not found") 





