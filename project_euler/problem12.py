#What is the value of the first triangle number to have over five hundred divisors?
import math

def triangle_divisors(n):
    i = 1
    sum = 0

    while True:
        sum += i

        if num_divisors(sum) > n:
            return sum

        i += 1

def num_divisors(n):
    
    if n == 1:
        num_divisors = 1
    else:
        num_divisors = 2

    for i in range(2, int(math.sqrt(n))):
        if (n % i == 0):
            num_divisors += 2
    
    return num_divisors

print(triangle_divisors(500))