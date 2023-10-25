attempt = 0
suma = 0
number = 1
while number != 0:
    number = int(input('Enter number: '))
    suma += number
    attempt += 1
print(f'RESULT: Quantity={attempt-1}, Sum={suma}, Mean={suma/(attempt - 1)}')


