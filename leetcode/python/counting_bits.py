from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp: List[int] = []

        if n == 0:
            return [0]

        if n == 1:
            return [0, 1]

        dp.append(0)
        dp.append(1)

        current_power_of_two = 2
        for i in range(2, n + 1):

            if current_power_of_two * 2 <= i:
                current_power_of_two *= 2

            dp.append(dp[i - current_power_of_two] + 1)

        return dp