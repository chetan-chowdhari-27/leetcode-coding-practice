#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    # a = list(map(int, a.split()))
    # b = list(map(int, b.split()))
    
    a_points = 0
    b_points = 0
    
    # Compare elements of a and b pairwise
    for i in range(len(a)):
        if a[i] > b[i]:
            a_points += 1
        elif a[i] < b[i]:
            b_points += 1
    
    concat = str(a_points) + str(b_points)
    return concat

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
