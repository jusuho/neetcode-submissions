#Bucket Sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        max_freq = 0
        for n in nums:
            f = freq.get(n, 0) + 1
            freq[n] = f
            if f > max_freq:
                max_freq = f
        
        buckets = [[] for _ in range(max_freq +1)]
        for num, f in freq.items():
            buckets[f].append(num)

        # 3) Gather top-k frequent elements from high to low frequency
        res = []
        for i in range(max_freq, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res