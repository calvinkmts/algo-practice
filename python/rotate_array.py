from typing import List
from copy import deepcopy

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        temp_nums = deepcopy(nums)
        for i in range(nums_length):
            new_position = (i + k) % nums_length
            nums[new_position] = temp_nums[i]

if __name__ == "__main__":
    solution = Solution()
    solution.rotate([1,2,3,4,5,6,7], 3)
