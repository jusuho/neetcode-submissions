class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        record = dict()
        for n in nums:
            result = record.get(n, None)
            if result is None:
                record[n]=1
            else:
                 return True
        return False
        