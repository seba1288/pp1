
 
def amount_to_pay(amount):
    count = 0
    five = amount//5
    count += amount % 5
    two = count//2
    count = count % 2
    one = count
    return five + two + one






print(amount_to_pay(27))
print(amount_to_pay(8))
print(amount_to_pay(2))
print(amount_to_pay(0))
