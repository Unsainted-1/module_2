numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    b = 0
    for j in range(1, len(numbers) + 1):
        a = i % j
        if a == 0:
            b = b + 1
    if b == 2:
        primes.append(i)
    else:
        if i != 1:
            not_primes.append(i)
print('Primes: ', primes)
print('Not Primes: ', not_primes)
