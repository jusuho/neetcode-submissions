class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1] * length

        # 第一遍：算出每個人左邊所有數的乘積
        prefix = 1
        for i in range(length):
            ans[i] = prefix
            prefix *= nums[i]
        
        # 第二遍：從右邊掃回來，同時乘上右邊所有數的乘積
        suffix = 1
        for i in range(length - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        
        return ans