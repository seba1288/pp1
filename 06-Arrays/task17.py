table = [[0,0,0],[0,0,0],[0,0,0]]

count = 0

for i in table:
    for j in i:
        
        i[count] = 1
        print(j,end=" ")
    count += 1
    print( '',end='\n')
print(table)