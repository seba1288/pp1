import math

circumference = int(input('enter circumference of tree: '))
r = circumference/(2*math.pi)
print(circumference)
print(round(r,2))
if r*2 >= 50:
    print(f'Tree can be cut down:{True}')
else:
    print(f'Tree can be cut down:{False}')
    





