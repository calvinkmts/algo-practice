from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])

        res = []

        for perm in perms: # permutations
            for i in range(len(perm) + 1):
                temp_perm = perm.copy()
                temp_perm.insert(i, nums[0])
                res.append(temp_perm)

        return res

