a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
print("Select the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice=int(input("Enter your choice (1/2/3/4): "))  
if choice==1:   
    print("The result of addition is: ", a+b)
elif choice==2:
    print("The result of subtraction is: ", a-b)
elif choice==3:
    print("The result of multiplication is: ", a*b)
elif choice==4:
    if b!=0:
        print("The result of division is: ", a/b)
    else:
        print("Error: Division by zero is not allowed.")
