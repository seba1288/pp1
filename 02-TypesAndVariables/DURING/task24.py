vehicle_number = input("enter vehicle_number: ")

letter1 = vehicle_number[0]
letter2 = vehicle_number[1]

if letter1 == 'K':
    if letter2 == 'K' or letter2 == 'R':
        print('Car from Krakow: ',True)
    else:
        print(False)
else:
    print(False)