
f = open('allproducts.txt','w')
f1 = open('MeatAndFish.txt','r')
f2 = open('GrainsAndBread.txt','r')

for i in f2:
    f.write(i)
for j in f1:
    f.write(j)
    