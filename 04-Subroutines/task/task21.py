import mymath,mykeyboard
gen = mymath.generate_number()
a = mykeyboard.read_number()
if a == gen:
    print('computer number: ',gen)
    print('You won the game!!')
else:
    print('computer number: ',gen)