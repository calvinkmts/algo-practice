from bisect import bisect_left
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        global_solution = []

        candidates.sort()

        def create_tree(level: int, current_sum: int, solution: List[int]):
            if current_sum == target:
                global_solution.append(solution)
                return

            if level == len(candidates) or current_sum > target:
                return

            current_num = candidates[level]

            # take the current element
            create_tree(level + 1, current_sum + current_num, solution + [current_num])

            while level < len(candidates) - 1 and candidates[level] == current_num:
                level += 1

            if candidates[level] == current_num:
                return

            # skip element and go to next
            create_tree(level, current_sum, solution)

        create_tree(0, 0, [])

        return global_solution