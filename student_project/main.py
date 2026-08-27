from student_result import calculate_tot
from student_result import calculate_percentage
from student_result import calculate_grade
n=int(input("Enter the number of subjects: "))
marks=[]
for i in range(n):
    mark=float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
total_marks=calculate_tot(marks)
percentage=calculate_percentage(marks)
grade=calculate_grade(percentage)
print("\nStudent Result")
print("Marks:", marks)
print("Total Marks:", total_marks)
print("Percentage:", round(percentage,2))
print("Grade:",grade)