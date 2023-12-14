import random


def rand_elem(array):
    ran = random.randrange(0,len(array))
    return array[ran]




print(rand_elem([2,3,4,5,67,6,]))