list1 = [-15, 8, -31, 47, -2, 19]

max = list1[0]
min = list1[0]
for i in list1:
    if i < min:
        min = i
    
    if i > max:
        max = i

print(max,min)
