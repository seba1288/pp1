



for number in range(1,31):
    if number % 5 == 0 and number % 3 == 0:
        print('BINGO')
    elif number % 5 == 0:
        print('FIVE')
    elif number % 2 == 0:
        print("THREE")
    else:
        print(number)