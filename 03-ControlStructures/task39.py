a = int(input("enter a: "))
b = int(input("enter b: "))


print(b*'*')
n =1
while n < a:
    print('*'+ (' ' * (b-2)) + '*')
    n += 1
print(b * '*')