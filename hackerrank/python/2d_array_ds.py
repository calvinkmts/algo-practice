#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):

    row, col = len(arr), len(arr[0])

    res = - 100000

    for i in range(1, row - 1):
        for j in range(1, col - 1):
            res = max(res, arr[i][j] + arr[i-1][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+1][j+1] + arr[i-1][j-1] + arr[i-1][j+1])

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
