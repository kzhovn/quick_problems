#What is the 10 001st prime number?

import math

def find_prime(n):
    primes_found = 0
    i = 1

    while True:
        if check_prime(i):
            primes_found += 1
            if (primes_found == n):
                return i

        i += 2

def check_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False

    return True

print(find_prime(10001))