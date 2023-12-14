l = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]


l[0] -= 1
l[-1] += 4
l[int(len(l)/2)] *= 2

l3 = []
print(l)
for i in l2:
    i += 3
    l3.append(i)
   


print(l2)
print(l3)

