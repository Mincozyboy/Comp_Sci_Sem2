x = int(input("Please enter first number: "))
z = str(input("Please enter an operator: "))
y = int(input("Please enter second number: "))
print(str(x) + str(z) + str(y) + ":") 
if (z == "+"):
    print(x+y)
elif(z == "-"):
    print(x-y)
elif(z == "*"):
    print(x*y)
elif(z == "%"):
    print(x%y) 