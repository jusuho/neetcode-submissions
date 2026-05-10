class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        for s in strs:
            sorted_str = "".join(sorted(s))
            if ans.get(sorted_str, None):
                ans[sorted_str].append(s)
            else:
                ans[sorted_str] = [s]
        return list(ans.values())