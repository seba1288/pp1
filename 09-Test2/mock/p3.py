def f(array2D):
    row_count = 0
    result = [0 for i in range(1,100)]
    for column in array2D:
        row_count = 0
        for number in column:
            result[row_count] += number
            row_count += 1
    n = 1
    while result[-n] == 0:
        result.remove(0)
    return result


print(f([[3,6,2,7], [9,5,4,0], [2,8,0,9]]) )


