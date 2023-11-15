def power(x, n):
    #: xn =  x * xn-1
    return x * (x**(n-1))


print(power(5,3))