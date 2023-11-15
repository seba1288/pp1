list1 = [0,1]

def cos(limit):
    n = 0
    while n < limit+10:
        list1.append(list1[n]+list1[n+1])
        n += 1
    return list1[limit-1]



print(cos(5))
print(cos(9))
print(cos(10))
print(cos(8))