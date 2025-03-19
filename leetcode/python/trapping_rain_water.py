from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0

        res = 0
        while left < right:

            if height[left] <= height[right]:
                temp = max_left - height[left]
                res += temp if temp > 0 else 0

                max_left = max(max_left, height[left])

                left += 1
            else:
                temp = max_right - height[right]
                res += temp if temp > 0 else 0

                max_right = max(max_right, height[right])

                right -= 1

        return res
