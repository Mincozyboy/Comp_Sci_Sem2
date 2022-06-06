x = int(input("How many items are you purchasing? "))
total = 0 
for i in range(0,x):
    item = input("What item are you purchasing? ")
    price = float(input("What's the price? "))
print("Thanks for buying "+ item)
total = total + price
print("Your total is: "+ str(total))