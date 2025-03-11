#!/bin/python3
import collections
import heapq
import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):

    leaderboard = {}

    pos = 2
    leaderboard[1] = ranked[0]
    for r in ranked[1:]:
        if r != leaderboard[pos-1]:
            leaderboard[pos] = r
            pos += 1

    res = []
    pointer = len(leaderboard)

    for p in player:
        while pointer > 0 and leaderboard[pointer] < p:
            pointer -= 1

        if pointer < 0:
            res.append(1)
        elif leaderboard.get(pointer) == p:
            res.append(pointer)
        else:
            res.append(pointer+1)

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
