table = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
suma_even = 0

for i in table:
    for j in i:
        if j % 2 == 0:
            suma_even += j

print(suma_even)
