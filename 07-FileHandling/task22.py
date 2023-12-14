import random

f = open('rndintagers','w')


for i in range(1,51):
    j = random.randrange(100,999)
    j = str(j) + '\n'
    f.write(j)


f.close()