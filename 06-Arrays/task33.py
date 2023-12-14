def even_odd(arr):
    result = []
    for i in arr:
        if i % 2 == 0:
            result.append(i)
    for j in arr:
        if j % 2 == 1:
            result.append(j)
    return result


    






print(even_odd([4,2,8,4,7,9,5]))