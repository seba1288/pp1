def f(name):
    acronym = ""
    counter = 0
    for letter in name:
        if letter == name[0]:
            acronym += letter
        
        elif letter == ' ':
            acronym += name[counter+1]
        counter += 1
    print(acronym)
    return acronym



print(f("Internet of Things") ,
f("For Your Information") ,
f("Python") 
)
