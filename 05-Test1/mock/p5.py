def f(binary_number):
    binary_number = str(binary_number)
    for digit in binary_number:
        if digit != '0' and digit != '1':
            return False
    else:
        return True
    




print(f("101101"))
print(f("1011201"))
print(f("1010b1"))

