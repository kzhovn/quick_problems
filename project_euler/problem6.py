#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += (i**2)

    return sum

def square_of_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    
    return sum**2

print(square_of_sum(100) - sum_of_squares(100))