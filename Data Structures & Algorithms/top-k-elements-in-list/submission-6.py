# 常規解法

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        array = sorted(counter.items(),key=lambda x: x[1], reverse=True)
        return [arr[0] for arr in array[:k]]