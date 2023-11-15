import math

print(math.log(5))
print(math.e**3)
print(math.sqrt(7))
print(math.sin(90))



print('task4 odp: d')
print('ABC ZAP ABC ODP D')


def computepay(hours,rate):
    hours = int(input('Enter Hours:'))
    rate = int(input('Enter Rate: '))
    pay = hours * rate
    return pay


def computegrade(score):
    if  1 >= score >= 0.9 :
        return 'A'
    elif 1 >=score >= 0.8:
        return 'B'
    elif 1 >= score >= 0.7:
        return 'C'
    elif 1 >= score >= 0.6:
        return 'D'
    elif 1 >= score < 0.6:
        return 'F'
    else:
        return "Bad score"
    

print(computegrade(0.66))