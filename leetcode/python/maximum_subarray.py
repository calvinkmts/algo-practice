class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [*nums]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])

        return max(dp)


    # def maxSubArray(self, nums: List[int]) -> int:
    #     max_sum = nums[0]
    #     curr_sum = 0
    #
    #     for num in nums:
    #         if curr_sum < 0:
    #             curr_sum = 0
    #         curr_sum += num
    #
    #         max_sum = max(max_sum, curr_sum)
    #
    #     return max_sum