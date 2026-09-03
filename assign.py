#reading the student records from file
print("Student Records")
with open("student.txt", "r") as file:
    for line in file:
        roll,name,course,marks = line.strip().split(",")
        print("Roll No:", roll )
        print("Name:", name)
        print("Course:", course)
        print("Marks:", marks)