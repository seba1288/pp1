def f(dict,x,y):
    suma = 0
    items = dict.values()
    for arr in items:
        for number in arr:
            if number in range(x,y+1):
                suma += number
    return suma







print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6) )