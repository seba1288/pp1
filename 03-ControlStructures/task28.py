bar_code = input('Enter EAN-13 article number: ')

if len(bar_code) == 13:
    print('Article number is correct')

if bar_code[0:3] == '590':
    print('Article manufactured in Poland')