from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        solution = -1
        biggest_temp_occurance = float("-inf")

        num_occurance = 1
        current_num = nums[0]

        for i in range(1, len(nums)):

            if nums[i] == current_num:
                num_occurance += 1
            elif nums[i] != current_num:
                if num_occurance > biggest_temp_occurance:
                    solution = current_num
                    biggest_temp_occurance = num_occurance
                num_occurance = 1
                current_num = nums[i]

        if num_occurance > biggest_temp_occurance:
            solution = current_num
            biggest_temp_occurance = num_occurance

        return solution

if __name__ == "__main__":
    solution = Solution()
    print(solution.majorityElement([3, 2, 3]))
    print(solution.majorityElement([2,2,1,1,1,2,2]))
