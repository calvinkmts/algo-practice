from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        left, right = 0, 0

        while right < len(nums) - 1:
            farthest_jump = -1
            for i in range(left, right + 1):
                farthest_jump = max(farthest_jump, i + nums[i])
            left = right + 1
            right = farthest_jump
            res += 1

        return res