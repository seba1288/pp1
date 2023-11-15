
def f(number):
    number = str(number)
    sum_num = 0
    for i in number:
        count = 0
        count = number.count(i)
        if count > 1:
            sum_num += int(i)
    return sum_num

           

    

print(f(1027))
print(f(230335))
print(f(513553007))



