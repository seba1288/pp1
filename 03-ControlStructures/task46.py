


list_of_numbers = []

for number in range(1,8):
    list_of_numbers.append(number)
    number1 = number
    while number1 < number +42:
        number1 += 7
        list_of_numbers.append(number1)
 
print(list_of_numbers[0:7])
print(list_of_numbers[7:14])
print(list_of_numbers[14:21])
print(list_of_numbers[21:28])
print(list_of_numbers[28:35])
print(list_of_numbers[35:42])
print(list_of_numbers[42:])
    

  
