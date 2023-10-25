
number1 = int(input('Enter number: '))


if number1 > 1:
   
    for i in range(2, int(number1/2)+1):
    
        if (number1 % i) == 0:
            print(number1, "is not a prime number")
            break
    else:
        print(number1, "is a prime number")
else:
    print(number1, "is not a prime number")
    


