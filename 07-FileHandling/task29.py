import re

f = open('grades.txt','r')
f1 = f.read()
r = re.findall('\d.\d',f1)
average = 0
print(r)
for i in r:
    average += float(i)

print(average/len(r))
    


