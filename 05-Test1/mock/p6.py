def f(number, even):
    sum_num = 0
    for i in str(number):
        if even == True:
            i = int(i)
            if i % 2 == 0:
                sum_num += i
        else:
            i = int(i)
            if i % 2 != 0:
                sum_num += i
    return sum_num



print(f(3124,True))
print(f(20576,False))