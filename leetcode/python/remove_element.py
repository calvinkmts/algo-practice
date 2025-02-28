from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [num for num in nums if num != val]
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeElement([3, 2, 2, 3], 3))
