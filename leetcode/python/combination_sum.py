from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        global_solution = []

        def create_tree(level: int, current_sum: int, solution: List[int]):
            print(solution)

            if level == len(candidates) or current_sum > target:
                return

            if current_sum == target:
                global_solution.append(solution)
                return

            # don't move the level (picking up the same element)
            create_tree(level, current_sum + candidates[level], solution + [candidates[level]])

            # move the level (add the next element)
            create_tree(level + 1, current_sum, solution)

        create_tree(0, 0, [])

        return global_solution