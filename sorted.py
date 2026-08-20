students=[("Amrutha",80),("Anusha",70),("Sravya",75),("Sravani",95)]
students=sorted(students,key=lambda x:x[1],reverse=True)
print("Students sorted by marks in descending order:")
for student in students:
    print(student)