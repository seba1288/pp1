def f(expression):
    suma = int(expression[0])
    
    counter = 0
    for i in expression[1:]:
        if i != '+' and i != '-':
            
            if expression[counter] == '+':
                suma += int(i)
            elif expression[counter ] == '-':
                suma -= int(i)
        counter += 1
    

    return suma 

print(f("2+3") )
print(f("3+8+1") )
print(f("2+3-4+5-0"))



