#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sum_arr = reduce(lambda x, y: x + y, arr)

    print(sum_arr - max(arr), sum_arr - min(arr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
