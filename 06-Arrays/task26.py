lis1 = [2 ,3 ,2 ,5 ,8 ,1 ,9 ,8]
uniqe = []


for i in lis1:
    count = 0
    for j in lis1:
      if j == i:
         count += 1
    if count == 1:
       uniqe.append(i)


print(uniqe)

