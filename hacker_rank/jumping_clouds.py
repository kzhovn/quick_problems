#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    num_jumps = 0
    i = 2

    if len(c) == 2:
        return 1

    while i <= len(c):
        if i == (len(c) - 2): #second to last
            return num_jumps + 1

        if c[i] == 0:
            num_jumps += 1
        elif c[i - 1] == 0:
            num_jumps += 1
            i -= 1
        else:
            return -1


        i += 2
        print("Index: " + str(i))


    return num_jumps

print(jumpingOnClouds([0, 1, 0]))
print(jumpingOnClouds([0, 1, 0, 0]))
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
print(jumpingOnClouds([0, 0]))

