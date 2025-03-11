from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        dp_include_first_house: List[int] = [0 for _ in range(len(nums))]
        dp_exclude_first_house: List[int] = [0 for _ in range(len(nums))]

        dp_include_first_house[0] = nums[0]

        if len(nums) == 1:
            return dp_include_first_house[0]

        dp_include_first_house[1] = max(nums[1], dp_include_first_house[0])
        dp_exclude_first_house[1] = nums[1]

        for i in range(2, len(nums)):

            if i == len(nums) - 1:
                dp_include_first_house[i] = max(dp_include_first_house[i - 2], dp_include_first_house[i - 1])
            else:
                dp_include_first_house[i] = max(nums[i] + dp_include_first_house[i - 2], dp_include_first_house[i - 1])

            dp_exclude_first_house[i] = max(nums[i] + dp_exclude_first_house[i - 2], dp_exclude_first_house[i - 1])

        return max(dp_include_first_house[len(nums) - 1], dp_exclude_first_house[len(nums) - 1])