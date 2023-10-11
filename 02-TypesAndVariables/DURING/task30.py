import random

dice_rolled = random.randrange(1,6)
print(f'Dice rolled: {dice_rolled}')
if dice_rolled == 6 or dice_rolled == 1:
    print(f'Special number:{True}')
else:
     print(f'Special number:{False}')