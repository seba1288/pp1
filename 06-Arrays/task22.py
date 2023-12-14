arr = [12, 6, 4, 9, 10]

def star(number_of_starts):
    return number_of_starts *'*'

for i in arr:
    print(f'{str(i)}: {star(i)}')