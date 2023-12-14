def bubblesort(array):
    n = len(array)
    for i in range(0,n-1):
        for j in range(0,n -i - 1):
            if array[i] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


print(bubblesort([5,4,6,7,9,12]))

