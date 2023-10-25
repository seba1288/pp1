list1 = [0,1]


n = 0
while n < 18:
    list1.append(list1[n]+list1[n+1])
    n += 1
print(list1)
