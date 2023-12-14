f = input("file name: ")
f += '.txt'
file = open(f'{f}','r')
lines = 0
for i in file:
    lines += 1

print(lines)