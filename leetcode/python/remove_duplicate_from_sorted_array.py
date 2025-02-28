from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([1,1,2]))
