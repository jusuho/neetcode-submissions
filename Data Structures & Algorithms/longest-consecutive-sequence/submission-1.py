class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        seen = set(nums)

        for n in nums:
            count = 0
            i = 0
            while n+i in seen: # n+1, n+2... until not exsit
                count += 1
                i += 1
            
            ans = max(ans, count)

        return ans

