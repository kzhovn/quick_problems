#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math

def largest_prime_factor(n):
    start = int(math.sqrt(n))
    for i in range(start, -1, -1):
        if (n % i == 0) and check_prime(i):
            return i

def check_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if (n % i == 0):
            return False

    return True

print(largest_prime_factor(600851475143))
