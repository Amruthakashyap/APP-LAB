#a student wants to analyze the marks of student using python statistics module
import statistics

marks = list(map(int, input("Enter marks for subjects separated by space: ").split()))

print("\n-----Statistical Analysis-----")
print("Marks:", marks)
print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))
print("Mode:", statistics.mode(marks))
print("Standard Deviation:", statistics.stdev(marks))