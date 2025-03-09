from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        global_height = 0
        global_solution = []

        def create_tree(level: int, solution: List[int]):
            if level == len(nums):
                global_solution.append(solution)
                return

            # don't add select the current element
            create_tree(level + 1, solution)

            # select the current element
            create_tree(level + 1, solution + [nums[level]])


        create_tree(global_height, [])

        return global_solution