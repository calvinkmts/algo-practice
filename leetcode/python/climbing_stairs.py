class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0] * 45

        dp[0] = 1
        dp[1] = 2

        n = n - 1 # because we use 0 index

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]