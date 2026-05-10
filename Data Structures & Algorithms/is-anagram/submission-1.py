class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = dict()
        for ss, tt in zip(s, t):
            seen[ss] = seen.get(ss, 0) + 1
            seen[tt] = seen.get(tt, 0) - 1

        for ele in seen.values():
            if ele is not 0:
                return False
        return True