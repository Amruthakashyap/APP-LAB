with open("student_records.txt", "r") as file:
    n=int(input("enter number of students"))
    for i in range(n):
        roll=input("enter roll number")
        name=input("enter name")
        course=input("enter course")
        marks=int(input("enter marks"))
        file.write(f"{roll},{name},{course},{marks}\n")
print("Student records saved")