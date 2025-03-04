from typing import List

class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        solution = [-1, -1]

        while left < right:

            total = numbers[left] + numbers[right]

            if total > target:
                right -= 1
            elif total < target:
                left += 1
            elif total == target:
                solution = [left + 1, right + 1]
                break

        return solution

    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hash_map = {}

        for i in range(len(numbers)):
            number = numbers[i]

            if number not in hash_map:
                hash_map[number] = [i]
            else:
                hash_map[number].append(i)

        for number in numbers:
            target_remainder = target - number

            if target_remainder not in hash_map:
                continue

            if target_remainder == number and len(hash_map[target_remainder]) > 1:
                solution = [hash_map[number][0] + 1, hash_map[number][1] + 1]
                return solution
            elif target_remainder == number and len(hash_map[target_remainder] < 2):
                continue
            else:
                solution = [hash_map[number][0] + 1, hash_map[target_remainder][0] + 1]
                return solution
    '''

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))
    print(solution.twoSum([2,3,4], 6))
    print(solution.twoSum([-1, 0], -1))
