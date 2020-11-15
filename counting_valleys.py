
#!/bin/python3
#Counting Valleys HackerRank
import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    level = 0
    level_old = 0
    valleys = 0
    path = list(path)

    for i in range(steps):
        level_old = level

        if path[i] == 'U':
            level += 1
        elif path[i] == 'D':
            level -= 1

        if level == 0 and level_old < 0:
            valleys += 1

    return valleys

print(countingValleys(2, "UD"))
print(countingValleys(8, "UDDDUDUU"))
