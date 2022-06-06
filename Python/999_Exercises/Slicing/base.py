x = input("What is your first and last name? ")
a = 1
for s in range (0,1):
    for i in range(0,len(x)):
        y=x[i:a]
        a=a+1
        print(y)
    print("")
    
