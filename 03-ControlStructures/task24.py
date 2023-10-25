price = 200.00
price_after = 140.00
discount = (price_after/price - 1) * -1

print(f'Current product price: {price_after}')
print(f'Previous product price{price}')

if discount >= 0.1:
    print('Buy the product!!')
print(f'Product price reduced by {int(discount * 100)} %')

