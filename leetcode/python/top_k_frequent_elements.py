from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_occurances = {}

        for num in nums:
            if num not in num_occurances:
                num_occurances[num] = 1
            else:
                num_occurances[num] += 1

        new_data_structure = sorted(list(num_occurances.items()), key=lambda x: x[1], reverse=True)

        solution = [num[0] for num in new_data_structure]

        return solution[:k]

if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1,1,1,2,2,3], 2))
    print(solution.topKFrequent([1], 1))
