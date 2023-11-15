
def range_neg_even(x,y):
    counter = 0
    for number in range(x,y+1):
        if number < 0 and number % 2 == 0:
            counter += 1
    return counter




print(range_neg_even(-7,8))
print(range_neg_even(-1,11))