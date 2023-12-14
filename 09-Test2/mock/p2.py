def f(human_age):
    dogs_age = 0
    human_age_2 = human_age - 2
    dogs_age = 4 * human_age_2 
    if human_age <= 2:
        return human_age * 10
    else:
        
        dogs_age = 4 * human_age_2 
        return dogs_age + 20
    
print(f(2),f(15))
