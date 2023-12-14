arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
l = []
for i in arr1:
    if i not in arr2:
        l.append(i)

print(l)
