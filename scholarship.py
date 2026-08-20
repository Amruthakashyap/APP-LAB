#a university provides a scholarship to students based on their marks and accept name using dictionary. Write a python program using lamda function to calculate the scholarship to the students above 80 marks
names = input("Enter the names of students separated by spaces: ").split()
marks = list(map(int, input("Enter the marks separated by spaces: ").split()))
students = dict(zip(names, marks))
scholarship = dict(filter(lambda x: x[1] > 80, students.items()))
print("Students eligible for scholarship:")
print(scholarship)
