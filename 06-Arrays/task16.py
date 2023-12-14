table = [[True,False],[True,True],[False,False]]


for i in table:
    count = 0
    for j in i:
        if j == True:
            j = False
            i[count] = j
            count += 1
        else:
            j = True
            i[count] = j
            count += 1


print(table)