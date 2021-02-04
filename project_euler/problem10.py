#Find the sum of all the primes below two million.
import math

def sum_primes(n):
    sum = 2
    for i in range(3, n, 2):
        if check_prime(i):
            sum += i
    return sum

def check_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False

    return True

print(sum_primes(2000000))