time24 = input('Enter time (24-hour format): ')
time12 = ''
time24_1 = int(time24[0:2])
time24_2 = int(time24[3:])
print(time24_1,time24_2)
if time24_2 > 60:
    print('to nie czas') 
elif time24_1 > 12:
    print(f'{time24_1-12}:{time24_2}pm')
else:
    print(f'{time24_1}:{time24_2}am')

