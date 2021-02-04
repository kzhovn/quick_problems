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
        

    print(bribes)
            
    
 1 3-2 4 1-2-2 = 3 
1 2 5 3 7 8 6 4
1 2 3 4 5 6 7 8
0 0 2-1 2 2-1-4

 1 3-2 4 1-4 2 = 5
1 2 5 3 7 8 4 6
1 2 3 4 5 6 7 8
0 0 2-1 2 2-3-2


6
-6

2 1 5 3 4
1 2 3 4 5
1-1 2-1-1

3
-3

