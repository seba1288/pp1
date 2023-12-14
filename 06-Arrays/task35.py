

def border(arr):
    count = 1
    print(len(arr)*5 * '-')
    for i in arr:
        print('|',end=' ')
        print(i,end='| ')
    print('')
    print(len(arr)*5* '-')




border([5,4,3,2,6,5,4,3,43,2])
