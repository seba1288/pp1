file = open('numbers.txt','r')


suma = 0
for i in file:
    i = int(i)
    suma += i
print(suma)