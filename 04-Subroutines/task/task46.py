def f(x,y):
    sum_of_num = 0
    for i in range(x,y+1):
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
            sum_of_num += i
    return sum_of_num


print(f(1,20))
print(f(10,30))






