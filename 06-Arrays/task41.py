arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

mul = 1
for i in arr:
    count = 1
    for j in range(len(i)):
        temp = i[j]
        temp = count * mul
        i[j] = temp
        print(temp, end=" ")
        count += 1
    print('')
    mul += 1



