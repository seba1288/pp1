import re


f = open('filecopy.txt','r')
f1 = f.read()
st = re.findall(r'\b[A-Za-z]{1,6}\b',f1)
print(st)
for i in st:
    print(i)