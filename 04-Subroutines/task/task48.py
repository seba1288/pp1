def f(product_code):
    three = 0
    for num in product_code[:-1]:
        num = int(num)
        three +=num
    reminder = three % 7
    if reminder == int(product_code[-1]):
        return True
    else:
        return False
    
print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))







