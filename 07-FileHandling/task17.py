f = open('loremipsum.txt','r')
n = 1
f1 = f.readlines()
for i in f1:
    if n % 5 == 0:
        enter = input('press enter: ')
    else:
        print(i.replace('\n',''))
    n += 1

f.close()
