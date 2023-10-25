
number = int(input('enter decimal number: '))
binary = ' '
number = number//2
q  = 1

while number != 0:
    
    if number % 2 == 1:
        binary += '1'
    else:
         binary += '0'
    number = number//2

bin_num = ''
print(binary)
n = 1
for num in binary:
   
    bin_num += binary[-n]
    n += 1
print(bin_num+'0')




