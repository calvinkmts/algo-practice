import math
from typing import List


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        min_banana_per_hour = 1
        max_banana_per_hour = max(piles)

        res = max_banana_per_hour

        while min_banana_per_hour <= max_banana_per_hour:

            mid_banana_per_hour = (min_banana_per_hour + max_banana_per_hour) // 2

            total_hr = 0
            for p in piles:
                total_hr += math.ceil(p / mid_banana_per_hour)

            if total_hr > h:
                min_banana_per_hour = mid_banana_per_hour + 1
            elif total_hr <= h:
                res = min(res, mid_banana_per_hour)
                max_banana_per_hour = mid_banana_per_hour - 1

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.minEatingSpeed([312884470], 312884469))