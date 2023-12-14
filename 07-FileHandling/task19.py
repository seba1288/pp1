

f = open('filecopy.txt','r')
f1 = open('copylines.txt','w')


for i in f:
    f1.write(i)


f.close()
f1.close()
