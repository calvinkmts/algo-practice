from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_product = [1 for _ in range(len(nums))]
        suffix_product = [1 for _ in range(len(nums))]

        prefix_product[0] *= nums[0]
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i]

        suffix_product[len(nums) - 1] *= nums[len(nums) - 1]
        for i in range(len(nums) - 2, 0, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i]

        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(suffix_product[i + 1])
            elif i == len(nums) - 1:
                res.append(prefix_product[i - 1])
            else:
                res.append(suffix_product[i + 1] * prefix_product[i - 1])

        return res



