#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
import math

def find_triplet_product(n):
    for a in range(1, n):
        for b in range(a + 1, n):
            c2 = a**2 + b**2
            c = math.sqrt(c2)
            if c.is_integer() and (a + b + c == n):
                return a * b *c

print(find_triplet_product(1000))


