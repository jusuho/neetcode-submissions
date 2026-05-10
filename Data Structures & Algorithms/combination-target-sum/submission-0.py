class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #DFS
        # edge case: sum > target, stop early
        # important: frequency
        ans = []
        def dfs(comb: List, start: int, total: int):
            if total == target:
                ans.append(comb[:])
                return
            if total > target:
                return

            for i in range(start, len(nums)):
                comb.append(nums[i])

                dfs(comb, i, total+nums[i])
                comb.pop() # backtrack
        
        dfs([], 0, 0)
        return ans
