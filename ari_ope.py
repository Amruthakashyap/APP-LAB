a = int(input("enter the value"))
b = int(input("enter the value"))

i=0
while(i==0):
    ch=int(input("enter your choice"))
    print("1.Addition:")
    print("2.Subtraction:")
    print("3.Multiplication:")
    print("4.Division:")
    print("5.Modulus:")
    print("6.Exit:")
    if ch==1:
        print("Addition",a+b)
    elif ch==2:
            print("Subtraction",a-b)
    elif ch==3:
        print("Multiplication",a*b)
    elif ch==4:
        print("Division",a/b)
    elif ch==5:
        print("Modulus",a%b)        
    elif ch==6:
        break 