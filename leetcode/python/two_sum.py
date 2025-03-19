from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for i in range(len(nums)):
            temp_value = target - nums[i]

            if temp_value in hash_map:
                return [hash_map[temp_value], i]
            else:
                hash_map[temp_value] = i

        return []


        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
