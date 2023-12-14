def subarr(arr1,arr2):
    for i in arr1:
        if i in arr2:
            continue
        else:
            return False
    return True




print(subarr([2,3,2,4,5],[2,3,4,3,2,6]))