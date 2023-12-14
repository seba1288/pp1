def create_2d_arr(x,y):
    zero = 0
    arr = []
    arr1 = []
    count = 1
    while count <= y:
        arr1.append(zero)
        count += 1
    count1 = 1
    while count1 <= x:
        arr.append(arr1)
        count1 += 1
    return arr




print(create_2d_arr(3,5))


