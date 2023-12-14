with open('data.txt','r')as file:
    file = file.read()
    file = file.split()

    def f(first_letter,last_letter):
        counter = 0
        for word in file:
            if word[0] == first_letter and word[-1] == last_letter:
                counter += 1
        return counter
    
    print(f('w','d'))
