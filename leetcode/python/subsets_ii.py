from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        global_solution = []

        nums.sort()

        def create_tree(level: int, solution: List[int]):
            if level >= len(nums):
                global_solution.append(solution)
                return

            current_num = nums[level]

            create_tree(level + 1, solution + [nums[level]])

            while level < len(nums) - 1 and current_num == nums[level]:
                level += 1

            create_tree(level, solution)




        create_tree(0, [])

        return global_solution