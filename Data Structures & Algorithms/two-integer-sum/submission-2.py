# HashMap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for index, n  in enumerate(nums):
            need = target - n #need=4, n=3
            if need in seen:
                return [seen.get(need), index]
            seen[n] = index
        return False