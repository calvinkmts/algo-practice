#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    pointer = 0
    jumps = 0

    while pointer < len(c) - 1:
        if pointer + 2 < len(c) and c[pointer + 2] == 0:
            jumps += 1
            pointer += 2
        elif pointer + 1 < len(c) and c[pointer + 1] == 0:
            jumps += 1
            pointer += 1

    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
