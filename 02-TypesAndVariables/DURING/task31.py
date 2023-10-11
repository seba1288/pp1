import random


number = random.randrange(1,6)
user_number = int(input("try to guess the computer number: "))
if number == user_number:
    print(True)
    print('congratulation you guesed right!')
else:
    print(False)
    print(f'the number was: {number}')
