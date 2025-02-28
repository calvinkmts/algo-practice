from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        solution = -1

        lower_bound : int = 1000000
        upper_bound : int = -1

        for price in prices:
            if price < lower_bound:
                lower_bound = price
                upper_bound = -1
            elif price > lower_bound and price - lower_bound > upper_bound - lower_bound:
                upper_bound = price

                solution = max(solution, upper_bound - lower_bound)

        return max(solution, 0)

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))
    print(solution.maxProfit([7,6,4,3,1]))
    print(solution.maxProfit([2,4,1]))
