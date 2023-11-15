def f(password):
    list1 = []
    for letter in password:
        if letter not in list1:
            list1.append(letter)
    count = len(list1)
    if count >= 6:
        return True
    else:
        return False
    

print(f("ax15") )
print(f("book123"))
print(f("A2water3") )
print(f("qwerty"))
print(f(""))





