x = int(input("Please enter line length: "))
y = str(input("Do you want horizontal or vertical line? (Answer is H or V) "))
if (y=="V"):
    for x in range(0,x):
        print("*")
if (y=="H"):
    for x in range(0,x):
        print("*",end="")
   