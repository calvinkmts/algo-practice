#!/bin/python3

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

    prev_height = -1
    current_height = 0

    num_of_valleys = 0

    for i in range(steps):

        if path[i] == "D":
            prev_height = current_height
            current_height -= 1

        elif path[i] == "U":
            prev_height = current_height
            current_height += 1

        if prev_height < current_height and current_height == 0:
            num_of_valleys += 1
            prev_height = -1
            current_height = 0

    return num_of_valleys



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
