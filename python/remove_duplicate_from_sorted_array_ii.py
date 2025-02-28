from typing import List

class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     nums_occurance : dict[int, int] = {}
    #     for num in nums:
    #         if num not in nums_occurance:
    #             nums_occurance[num] = 1
    #         else:
    #             nums_occurance[num] += 1

    #     new_nums_length = 0
    #     for num in nums_occurance.keys():
    #         end_cursor = nums_occurance[num] if nums_occurance[num] <= 2 else 2

    #         if end_cursor == 1:
    #             nums[new_nums_length] = num
    #         elif end_cursor == 2:
    #             nums[new_nums_length] = num
    #             nums[new_nums_length + 1] = num

    #         new_nums_length += end_cursor

    #     return new_nums_length
    #

    def removeDuplicates(self, nums: List[int]) -> int:
        cursor = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[cursor-2]:
                nums[cursor] = nums[i]
                cursor += 1

        return cursor


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([1, 1, 1, 2, 2, 3]))
