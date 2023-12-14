def median(array):
    l = len(array)
    if len(array) % 2 == 1:
        return l
    else:
        mid1 = array[int(l/2)]
        mid2 = array[int(l/2)-1]

        return (mid1 + mid2)/2
    


print(median([1,0,9,4,6,7]))
print(median([6,8,3,1,0,5,7]))