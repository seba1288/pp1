def compare(arr1,arr2):
    if arr1 == arr2 and len(arr1) == len(arr2):
        return 'array1: ', arr1 , 'array2: ', arr2
    else:
        return False



print(compare(["water","book","sky"]  , ["water","book","sky"]))
#[True,False]   [True,False,True]
print(compare([5,3,1],   [5,3,2]))
#[3,2,1]   [3,2]
