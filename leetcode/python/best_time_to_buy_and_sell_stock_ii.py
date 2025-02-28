from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        solution = 0
        temp_solution = -1

        lower_bound : int = 1000000
        upper_bound : int = -1

        for price in prices:
            if price < lower_bound or price < upper_bound:
                # print(f"lower_bound {price}")
                if upper_bound != -1:
                    # print(f"special lower_bound {price}")
                    solution += temp_solution
                    temp_solution = -1
                lower_bound = price
                upper_bound = -1
            elif price > lower_bound and price - lower_bound > upper_bound - lower_bound:
                # print(f"upper_bound {price}")
                upper_bound = price
                temp_solution = max(temp_solution, upper_bound - lower_bound)

        if temp_solution != -1:
            solution += temp_solution

        return solution

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))
    print(solution.maxProfit([1,2,3,4,5]))
    print(solution.maxProfit([7,6,4,3,1]))
