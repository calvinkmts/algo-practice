from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1

        res_area = -1
        while left < right:

            area = (right - left) * min(height[left], height[right])
            res_area = max(res_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res_area
