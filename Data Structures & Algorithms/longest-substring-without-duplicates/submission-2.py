class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        seen = set()
        l = 0

        for i, ss in enumerate(s):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(ss)
            ans = max(ans, len(seen))
        return ans