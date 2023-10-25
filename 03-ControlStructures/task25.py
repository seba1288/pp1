products = int(input("Number of products purchased "))
prices = float(input(" Product price:  "))
discounted =  prices * 0.75
n = 1
pay = 0
while  n <= products:
    if n > 2:
        pay += discounted
    else:
     pay += prices
    n += 1
print(pay)





