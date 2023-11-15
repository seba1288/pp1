

def aster_slash(number):
    g = 1
    if number == 1:
        return "*"
    while g <= number :
        if number == 1:
            print( "\n*")
        print('*', end="/")
        g += 1
    

aster_slash(4)
print('\n')
print(aster_slash(1))