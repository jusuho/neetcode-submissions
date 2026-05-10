class Solution:
    def rob(self, nums: List[int]) -> int:
        # can rob or not depend on the previous house robbed or not
        # rob => how much can get

        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        if len(nums) == 1:
            return nums[0]
            
        dp = [0] * len(nums)
        dp[0] = nums[0]
        # dp[1] = nums[1]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp.pop()