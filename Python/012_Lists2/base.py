import random
thislist = []
x = int(input("How many random numbers would you like?"))
for l in range(0,x):
    r = random.randrange(10)
    thislist.append(r)
print(str(thislist))
    