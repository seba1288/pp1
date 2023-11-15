def f(text):
    text1 = '""'
    for letter in text:
        if len(text)  != 1 and len(text) != 0:
            text1 = print(letter, end='-')
        else:
            return text
    return text1




print(f("Univesity"))
print(f("UE") )
print(f("x") )
print(f("") )
