class Solution:

    def encode(self, strs: List[str]) -> str: 
        # given strs = ["hello", "wor#ld"]
        res = ""
        for s in strs: # O(N)
            res += str(len(s))+'#'+s # 5#hello, 6#wor#ld
        return res

    def decode(self, s: str) -> List[str]:
        # given s = 5#hello6#wor#ld, len = 15
        res = []
        i = 0
        while i < len(s):
            j = i # j = 0
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # j = 1, length = 5
            res.append(s[j + 1:j + 1 + length])

            i = j + 1 + length # i = 7
        return res
