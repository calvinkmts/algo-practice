from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        unique_seq = sorted(list(set(nums)))

        solution = -1

        temp_consequtive_length = 1
        for i in range(1, len(unique_seq)):
            if unique_seq[i] - unique_seq[i-1] == 1:
                temp_consequtive_length += 1
            elif unique_seq[i] - unique_seq[i-1] > 1:
                solution = max(solution, temp_consequtive_length)
                temp_consequtive_length = 1

        solution = max(solution, temp_consequtive_length)

        return solution

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100,4,200,1,3,2]))
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(solution.longestConsecutive([1,0,1,2]))
