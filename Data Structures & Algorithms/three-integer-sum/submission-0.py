class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # reduce to N times of 2sum
        # a + b + c = 0
        # => a + b = -c (2 sum)
        ans = []
        nums.sort() # O(nlogn)

        for i, a in enumerate(nums):
            # if a > 0, the later elements will be greater, so it is impossible be answer
            if i > 0 and a == nums[i-1]: # in case of duplicated answers
                continue
            
            # 2 sum
            l = i + 1
            r = len(nums) - 1

            while l < r :
                result = a + nums[l] + nums[r]
                if result > 0:
                    r -= 1
                elif result < 0:
                    l += 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # 關鍵：如果新位置的數字跟剛剛左邊 (l-1) 一樣，就繼續往右走
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    # 同理，如果右邊 (r+1) 一樣，就繼續往左走
                    # (其實只要處理 l 或 r 其中一邊就能避免重複，但保險起見兩邊都寫也沒問題)
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return ans