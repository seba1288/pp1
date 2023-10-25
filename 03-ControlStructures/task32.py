#Are you interested in computer science? (Y/N): Y 
#Do you like playing computer games? (Y/N): N
#Do you have an Instagram account? (Y/N): Y
#Interested in computer science: Yes
#Playing computer games: No
#Has an Instagram account: Yes

computer_science = input('Are you interested in computer science? (Y/N): ')
computer_games = input('Do you like playing computer games? (Y/N): ')
instagram = input('Do you have an Instagram account? (Y/N): ')


if computer_science == 'Y':
    computer_science = True
    print('Interested in computer science: Yes')
else:
    computer_science = False
    print('Interested in computer science: No')

if computer_games == 'Y':
    computer_games = True
    print('Playing computer games: Yes')
else:
    computer_games = False
    print('Playing computer games:  No')

if instagram == 'Y':
    instagram = True
    print('Has an Instagram account:  Yes')
else:
    instagram = False
    print('Has an Instagram account:  No')


