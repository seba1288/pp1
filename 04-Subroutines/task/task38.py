

def f(palindrome):
    minmum = 1
    for letter in palindrome:
        if letter == palindrome[-minmum]:
            minmum += 1
        else:
            return False
    return True


print(f("radar") )
print(f("12-11-21") )
print(f("book") )