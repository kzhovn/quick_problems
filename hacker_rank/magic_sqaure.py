#You will be given a [3 x 3] matrix s of integers in the inclusive range [1, 9]. 
#We can convert any digit a to any other digit b in the range [1, 9] at cost of |a- b|. 
#Given s, convert it into a magic square at minimal cost & print cost

#http://www.mathematische-basteleien.de/magsquare.htm

#Stupid brute force solution is to check all the options and take the cheapest.
#Only 8 so I don't actually think this is worse than most possible options?
#Too lazy to actually code this it sounds boring, just check each (non-middle) cost,
#compare, take lowest, add middle cost, print.

def formingMagicSquare(s):
    cost = 0

    #middle is always 5
    if (s[2][1] != 5):
        cost = abs(s[2][1] - 5) 
        s[2][1] = 5


    







print(formingMagicSquare([[4 9 2], [3, 5, 7], [8 1 5]])) #cost 1
print(formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]])) #cost 7
print(formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]])) #cost 4