from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        fuel = nums[0]
        pointer = 1

        while fuel > 0 and pointer < len(nums):
            fuel -= 1
            fuel = max(fuel, nums[pointer])
            pointer += 1

        if pointer == len(nums) - 1:
            return True

        return False