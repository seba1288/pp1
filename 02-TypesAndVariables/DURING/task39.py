price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))
discounted = price * (discount/100)

print(f'Price with discount: {round(price - discounted ,2)}')
print(f'Reduction: {round(discounted , 2)}')

