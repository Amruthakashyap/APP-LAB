#sum of n numbers using recursion
sum=0
def sum(a,b):
    if a==b:
        return a    
    else:
        return a+sum(a+1,b)
print(sum(1,20))