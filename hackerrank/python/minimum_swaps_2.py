#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    pointer = 0

    swaps = 0
    while pointer < len(arr):
        if arr[pointer] != pointer + 1:
            temp = arr[pointer] # current pointer value
            arr[pointer] = arr[arr[pointer] - 1] 
            arr[temp-1] = temp
            swaps += 1
        else:
            pointer += 1

    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
