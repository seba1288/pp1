def betw(x,y):
    number = int(input('A number: '))
    if x <= number <= y:
        return True
    else:
        return False

print(betw(2,15))