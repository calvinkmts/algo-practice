#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):

    str_length = len(s)

    mul = n // str_length
    remainder = n % str_length

    num_a_in_s = 0
    for c in s:
        if c == "a":
            num_a_in_s += 1

    total_a = num_a_in_s * mul

    remainder_a = 0
    for i in range(remainder):
        if s[i] == "a":
            remainder_a += 1

    return total_a + remainder_a



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
