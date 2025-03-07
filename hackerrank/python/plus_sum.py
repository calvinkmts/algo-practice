#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    arr_size = len(arr)

    positive_nums_count = list(filter(lambda x: x > 0, arr))
    zero_nums_count = list(filter(lambda x: x == 0, arr))
    negative_nums_count = list(filter(lambda x: x < 0, arr))

    print("%.6f" % (len(positive_nums_count) / arr_size))
    print("%.6f" % (len(negative_nums_count) / arr_size))
    print("%.6f" % (len(zero_nums_count) / arr_size))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
