l = [2, 3, 7, 5, 4]


print(l,len(l),l[0],l[1],l[2],l[-1],l[-2],(l[0]+l[-1]),l[int(len(l)/2)],)



for i in l:
    print(i,end=" ")


index = 0
while index <= (len(l)/2):
    print(l[index])
    index += 1