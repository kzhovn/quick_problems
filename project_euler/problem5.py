#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divide_twenty():
    i = 2520
    while True:
        div = True
        for j in range(2, 20):
            if (i % j != 0):
                div = False
        if div == True:
            return i

        i += 20

print(divide_twenty())