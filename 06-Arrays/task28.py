arr = [5,1,9,6,1]

max1 = max(arr)


for i in arr:
    if i == max1:
        arr.remove(i)
print(max(arr))
    


