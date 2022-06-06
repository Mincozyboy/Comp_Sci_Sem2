Symbol = input("What symbol would you like to use? ")
x = int(input("Please enter width length: "))
y = int(input("Please enter height length: "))

for l in range(0,y):
    for s in range(0,x):
        print(Symbol,end="")
    print("")