from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [ans[0] for ans in Counter(nums).most_common(k)]