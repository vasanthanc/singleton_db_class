from math import sqrt; from itertools import count, islice

def Primes(max):
    number = 1
    while number < max:
        number += 1
        if check_prime(number):
            yield number

def check_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


primes = Primes(1000)
print(primes)

for x in primes:
    print(x)