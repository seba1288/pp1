text = 'An apple a day keeps the doctor away'
arr = text.split(' ')

def Mytext(text):
    count = 1
    for i in text:
        if i == ' ':
            count += 1
    return count

#def long_short(arr):
        
    



print()
print(Mytext(text))
print(sorted(arr,key=len))