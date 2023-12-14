f = open('intager power','w')


for i in range(1,11):
    i2 = i**2
    i3 = i**3
    i = str(i) + ',' + str(i2) + ',' + str(i3) + '\n'
    f.write(i)


f.close()