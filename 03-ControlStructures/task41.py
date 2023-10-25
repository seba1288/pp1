
atemmpt = 0
pin = '0805'
while atemmpt < 3:
    pin_1 = input('Enter the PIN code: ')
    if pin_1 != pin:
        print('Incorrect...')
    else:
        print('Correct')
        break
    atemmpt += 1
if pin_1 != pin:
    print('Sorry, your payment card has been blocked.')


