import digits19

number = int(input("Enter a number: "))
sum_d = digits19.sum_digits(number)
msg = f"Sum of digits {number} is {sum_d}"
print(msg)
