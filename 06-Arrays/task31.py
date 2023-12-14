def greater(arr):
    number = int(input("number: "))
    result = []
    for i in arr:
        if number < i:
            result.append(i)
    return result




print(greater([6,8,3,1,0,5,7]))
