#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        if q[i] > i + 3:
            print("Too chaotic")
            return
        elif q[i] == i + 3:
            bribes += 2
        elif q[i] == i + 2:
            bribes += 1
        elif i != len(q) - 1 and q[i] > q[i + 1]:
            bribes += 1

    print(bribes)
            
    

1 2 5 3 7 8 6 4
1 2 3 4 5 6 7 8