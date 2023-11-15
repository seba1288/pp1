def prime_numbers(n,w):
    primes = []
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return  primes[w-1]

prime_list = prime_numbers(50,5)
print(prime_numbers(50,1))
print(prime_numbers(50,5))

