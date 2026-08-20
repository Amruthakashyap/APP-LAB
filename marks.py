marks=list(map(int,input("Enter the marks separated by spaces: ").split()))
updated_marks=list(map(lambda x:min(x+5,100), marks))
print("original marks:", marks)
print("updated marks:", updated_marks)