def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
print(sum_digits(7182))
print(sum_digits(0))
print(sum_digits(333))
