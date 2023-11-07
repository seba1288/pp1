def f(name):
    acronym = name[0]
    for i in range(1,len(name)):
        if name[i-1] == " ":
            acronym += name[i]
    return acronym

