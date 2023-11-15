



def even_number(number, even):
    number = str(number)
    sum_even = 0
    sum_odd = 0
    if even == True:
        for digit in number:
            digit = int(digit)
            if digit % 2 ==0:
                sum_even += digit
        return sum_even
    else:
        for digit in number:
            digit = int(digit)
            if digit % 2 ==0:
                sum_even += digit
            else:
                sum_odd += digit
        return sum_odd

print(even_number(3124,True))
print(even_number(3124,False))
print(even_number(20576,False))
print(even_number(20576,True))
print(even_number(13115,True))